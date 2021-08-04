# Dependencies
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import json
import os

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///titanic.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Animal = Base.classes.passenger


#################################################
# Flask Setup
#################################################

# Create app
app = Flask(__name__)

# Load JSON
animals_filepath = os.path.join(".", "api", "api_structs", "animals.json")
countries_filepath = os.path.join(".", "api", "api_structs", "countries.json")
habitats_filepath = os.path.join(".", "api", "api_structs", "habitats.json")
threats_filepath = os.path.join(".", "api", "api_structs", "threats.json")

# Loads JSON files and stores in dict
with open(animals_filepath) as jsonfile:
    animals_json = json.load(jsonfile)
    
    animals = animals_json["animals"]

# Loads JSON files and stores in dict
with open(countries_filepath) as jsonfile:
    countries_json = json.load(jsonfile)
    
    countries = countries_json["countries"]

# Loads JSON files and stores in dict
with open(habitats_filepath) as jsonfile:
    habitats_json = json.load(jsonfile)
    
    habitats = habitats_json["habitats"]

# Loads JSON files and stores in dict
with open(threats_filepath) as jsonfile:
    threats_json = json.load(jsonfile)
    
    threats = threats_json["threats"]



#################################################
# Flask Routes
#################################################

@app.route('/api/v1/animals')
def getAllAnimals():
    return jsonify(animals)

@app.route('/api/v1/countries')
def getCountries():
    return jsonify(countries)

@app.route('/api/v1/habitats')
def getHabitats():
    return jsonify(habitats)

@app.route('/api/v1/threats')
def getThreats():
    return jsonify(threats)