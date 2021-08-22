# imports
import flask
from flask import request, Response
import numpy as np
import pandas as pd
import pickle 
import tensorflow as tf

# load text preprocessing
from preprocessing import * 

# load models
outcome_model = tf.keras.models.load_model('models/outcome')
intent_model = tf.keras.models.load_model('models/intent')

# load TF-IDF vectorizer object for outcome model
with open('models/outcome/tfidf.pickle', 'rb') as data:
    outcome_tfidf = pickle.load(data)

# load TF-IDF vectorizer object for intent model
with open('models/intent/tfidf.pickle', 'rb') as data:
    intent_tfidf = pickle.load(data)

# initialize application
app = flask.Flask(__name__)

# default route not used
@app.route('/', methods=['GET'])
def home():
    return "<p>no endpoint. use api/outcome or api/intent</p>"

# route for the outcome prediction.
@app.route('/api/outcome', methods=['POST'])
def api_outcome(): 

    # load message for outcome prediction
    msg = request.form['message']

    # convert text to vector
    vector = prepare_message([msg], outcome_tfidf)

    # run outcome prediction model
    prediction = outcome_model.predict(vector)[0][0] * 100

    return str(prediction)

# route for intent recognition.
@app.route('/api/intent', methods=['POST'])
def api_intent(): 

    # load message for intent recognition
    msg = request.form['message']

    # list of intents
    intents = ['finance','inventory','stop','trade']

    # convert text to vector
    vector = prepare_message([msg], intent_tfidf)

    # run intent recognition model
    prediction = intents[intent_model.predict(vector).argmax(axis=1)[0]]

    return str(prediction)

  
