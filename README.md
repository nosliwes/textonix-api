# Textonix-api

The api is a flask application that contains the outcome prediction model and the intent classification model.  

Steps to run:
1. Deploy the api to an app service.
2. Start the api by using flask run.

After the api is running, the api exposes two endpoints, one for outcome prediction and one for intent classification.

### Outcome Prediction

Outcome prediction exposes a <b><i>POST</i></b> method accepting one form field named <b><i>message</i></b>.

As an example, if running on localhost, the endpoint is

http://127.0.0.1:5000/api/outcome

The result is a string value representing the probability for a sucessful outcome.

### Intent Classification

Intent recognition exposes a <b><i>POST</i></b> method accepting one form field named <b><i>message</i></b>.

As an example, if running on localhost, the endpoint is

http://127.0.0.1:5000/api/intent

The result is a string value of the recoginized intent.  

There are four possible intents, <b>finance</b>, <b>trade</b>, <b>inventory</b>, or <b>stop</b>.

### Deployment

A testing endpoint is deployed to https://textonix-api.azurewebsites.net/


