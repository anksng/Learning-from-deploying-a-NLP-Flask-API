import numpy as np
from flask import Flask, request, jsonify, render_template,redirect
#import pickle
#from predict import predict
from utils import utils
from models import models
import pandas as pd

app = Flask(__name__)

tag_to_ix ={'O': 0,  'date_of_departure': 1, 'date_of_return': 2,  'taxes': 3,  'cost_of_trip': 4,  'date_of_booking': 5}
class Config_SOFTMAX(object):
    '''LSTM'''
    embedding_dim = 100
    hidden_dim = 100
    num_layer = 1
    embedding_model = utils.load_embedding_model('model_complete.bin')
    use_fasttext = True  # if false model will inititalize embedding layer
    #    vocab_size = len(word_to_ix)   #fiix
    tagset_size = 6

    '''Paths'''
    path_to_saved_model = '/home/ankit/experiment_framework/saved_models/'
    dropout = 0.5

    use_softmax = True


'''Init model'''
config_soft = Config_SOFTMAX()
embedding_model = utils.load_embedding_model('model_complete.bin')

model = models.LSTMTagger_softmax(config_soft,1000,tagset_size=6,embedding_model=embedding_model)

'''Loading model'''
model = utils.load_model(model,'model99.pt')



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    text = request.form.get('Text')
    data = np.array(text.split(' '))
    scores = model(data)
    pred = [i for i in utils.get_tags(scores.detach().numpy())]
    index_to_tag = utils.invert_mapping(tag_to_ix)
    predictions = []
    for i in pred:
        predictions.append(index_to_tag[i])

    results = []
    for i in range(len(pred)):
        if predictions[i] != 'O':
            results.append([predictions[i], data[i]])
    results_ = pd.DataFrame(results, columns=['label', 'entity'])
    if len(results_)>0:
        return render_template('result.html', TEXT= text,RESULTS=results_)
    else:
        return render_template('notfound.html',TEXT=text, RESULTS = 'Sorry! No entities were detected')


@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)