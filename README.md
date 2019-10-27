# Learnings-from-deploying-a-NLP-flask-api



## Prediction Service : 
The idea of this project was to learn steps which are needed to deploy an application which can be used by any user (not only locally). This `FLASK api` provides a pre-trained `NLP model` written in `pytorch`. The end result is - <br/>

#### 1. Paste text in the browser from which the entites have to be extracted.
![](images/first.png)
#### 2. The browser GUI runs a pre-trained model to detect entites. Press `predict` button to run prediction using the backened `BILSTM-CRF` model
![](images/second.png)
#### 3. Results containing detected entities and their labels are displayed in the browser

![](images/third.png)

#### If no entities found : 

![](images/fourth.png)


## Model outline : 

![](images/flaskmodel.png)


The aim is to deploy the application as a service using Flask and share the working browser application as a running container  of a docker image, hence can be used by a remote client with ease. In doing so, I gained some insights which can be useful in developing such an application from Data Science and Backend perspective which are presented below. <br/>

The three major elements of this application are:
* **NLP model**
* **Flask app**
* **Running as a Container - Docker**
