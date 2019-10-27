from alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip 
    
WORKDIR /app

COPY . /app

RUN cat requirements.txt | xargs -n 1 pip install


