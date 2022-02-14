
# Serverless Framework Python Flask API OmniNext Test

Implementation of Rest API for the creation and display of the user model, In particular focusing on create the following endpoints with the respective methods for writing and reading on the DB:

    createUser

    getUserById


## Requirements

- python3.9
- npm
- AWS CLI
- serverless framework


## Install 

First install serverless-python-requirements and serverless-wsgi, both are already in devDependencies inside our package.json.
To install them go in the project main directory using npm:

> npm install

Then create a virtual environment and activate it. I'm using Python3.9 as runtime environment:

> virtualenv venv --python=python3

Activate it:
	
> source venv/bin/activate


## Deploy functions:

Taking for granted that the reader has linked IAM with AWS CLI, and has already configured serverless, just run:
	
> sls deploy

Since we're storing Users in a database. We want to store them by userId, which is a unique identifier for a particular user.

I'll use curl for these examples. Set the DOMAIN variable to your unique domain and base path so it's easier to reuse:

Set the DOMAIN variable to your unique domain and base path so it's easier to reuse:

> export DOMAIN=YOURDOMAIN

In my case:

> export DOMAIN=https://n51iverkzf.execute-api.us-east-1.amazonaws.com/dev

Now let's add a new user:
	
> curl -H "Content-Type: application/json" -X POST ${DOMAIN}/users -d '{"userId": "ID", "name": "NAME"}'

The output should be like this:
	
    "userId": "ID",

    "name": "NAME"
    
  
I've already insert some tables, you can check them using curl:

> curl -H "Content-Type: application/json" -X GET ${DOMAIN}/users/keewee

Or directly in your browser:

> https://n51iverkzf.execute-api.us-east-1.amazonaws.com/dev/users/keewee
