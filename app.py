# 1. Import Flask
from flask import Flask

#################################################
# Make 'measurement' table a Dictionary
#################################################


#################################################
# Make 'station' table a Dictionary
#################################################


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
        f"Welcome to the Gary's Homwork homepage <br/>"
        f"Avaialable routes:<br/>"
        f"/api/v1.0/percipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

# Percipitation API Page
@app.route("/api/v1.0/percipitation")
def percipitation():
   
    return jsonify(prcp)

# Stations Page
@app.route("/api/v1.0/stations")
def stations():
    
     return jsonify(station)

 # Observed temperature Page
@app.route("/api/v1.0/tobs")
def stations():
    
     return jsonify(tobs) 

@app.route("/api/v1.0/<start>")
def vacation start date (start):
    """Return a JSON list of the minimum temperature, the average temperature, 
    and the max temperature for a given start or start-end range."""
    """When given the start only, 
    calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date."""

    canonicalized = start.replace(" ", "").lower()
    for xxx in xxx:
        xx = xx["start"].replace(" ", "").lower()

        if search_term == canonicalized:
            return jsonify(xxx)

    return jsonify({"error": f"Start date {start} not found."}), 404   

@app.route("/api/v1.0/<start>/<end>")
def vacation start date (start):
    """Return a JSON list of the minimum temperature, the average temperature, 
    and the max temperature for a given start or start-end range."""
    """When given the start and the end date, calculate the TMIN, TAVG, 
    and TMAX for dates between the start and end date inclusive."""

    canonicalized = start.replace(" ", "").lower()
    for xxx in xxx:
        xx = xx["start"].replace(" ", "").lower()

        if search_term == canonicalized:
            return jsonify(xxx)

    return jsonify({"error": f"Start date {start} not found."}), 404  


# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
