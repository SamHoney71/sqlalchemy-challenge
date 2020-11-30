#########Import Flask, sqlalchemy, pandas and other dictionaries###############
from flask import Flask, jsonify
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import datetime as dt


# reflect an existing database into a new model
# reflect the tables
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn = engine.connect()

# Declare a Base using `automap_base()`
Base = automap_base()

# Use the Base class to reflect the database tables
Base.prepare(engine, reflect=True)

# Assign the measurement class & station class to variables called `Measurement` & 'Station'
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session to link Python to database
session = Session(engine)

# Save references to perciptiation & date table & convert to dictionary
date_prcp_df = pd.read_sql("SELECT date, prcp FROM Measurement", conn)
date_prcp_dic = date_prcp_df.to_dict('records')


# Save references to Station table & convert to a dictionary
station_df = pd.read_sql("SELECT * FROM Station", conn)
station_dic = station_df.to_dict('records')

#Save all references to measurement table & convert to a dictionary
measurement_df = pd.read_sql("SELECT * FROM Measurement", conn)
measurement_dic = measurement_df.to_dict('records')

 
 # Query the dates and temperature observations 
 # of the most active station for the last year of data.
engine.execute('SELECT * FROM Measurement')

sel_2 = [Measurement.date, Measurement.tobs]
hi_station_12mo_temp = session.query(*sel_2).\
    filter(func.strftime(Measurement.date) > "2016-08-23").\
    filter_by(station = 'USC00519281').all()
hi_station_temp_df =pd.DataFrame(hi_station_12mo_temp)
hi_station_temp_df['date'] = pd.to_datetime(hi_station_temp_df['date'])
hi_station_temp_dic = hi_station_temp_df.to_dict('records')

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

#Home page
@app.route("/")
def welcome():
    return (
        f"Welcome to the Gary's Homework homepage <br/><br/>"
        f"Available routes:<br/><br/>"
        f"/api/v1.0/percipitation<br/>"
        f"<br/>"
        f"/api/v1.0/stations<br/>"
        f"<br/>"
        f"/api/v1.0/tobs<br/><br/>"
        f"/api/v1.0/start_date/<date>"
        f" (Note: Enter start date after'/' in YYYY-MM-DD format.) <br/> <br/>"
        f"/api/v1.0/start_date/end_date/<end_date> "
        f"   (Note: Enter start date after'/' and then end date after'/' in YYYY-MM-DD format.)<br/>"
    )

# Percipitation & dates API Page
@app.route("/api/v1.0/percipitation")
def percipitation():
    """Return date and percipitation data as a json"""
   
    return jsonify(date_prcp_dic)

# Stations Page
@app.route("/api/v1.0/stations")
def stations():
    
     return jsonify(station_dic)


@app.route("/api/v1.0/tobs")
def hi_station_observed_temp():
    
     return jsonify(hi_station_temp_dic) 

# @app.route("/api/v1.0/start_date/<date>")
# def measurement_date (date):
#     # """Return a JSON list of the minimum temperature, the average temperature, 
#     # and the max temperature for a given start or start-end range."""
#     # """When given the start only, 
#     # calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date."""

#     canonicalized = date.replace()
#     for date in measurement_df:
#         search_term = measurement_dic[{"date"].replace()

#         if search_term == canonicalized:
#             return jsonify(measurement_dic)

#     return jsonify({"error": f"Start date {date} not found."}), 404   

# @app.route("/api/v1.0/start_date/end_date/<end_date>")
# def vacation start date (start):
#     """Return a JSON list of the minimum temperature, the average temperature, 
#     and the max temperature for a given start or start-end range."""
#     """When given the start and the end date, calculate the TMIN, TAVG, 
#     and TMAX for dates between the start and end date inclusive."""

#     canonicalized = start.replace(" ", "").lower()
#     for xxx in xxx:
#         xx = xx["start"].replace(" ", "").lower()

#         if search_term == canonicalized:
#             return jsonify(xxx)

#     return jsonify({"error": f"Start date {start} not found."}), 404  


# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
