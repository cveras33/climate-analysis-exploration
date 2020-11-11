import datetime as dt 
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite") 

Base = automap_base()
Base.prepare(engine, reflect = True)

Measurement = Base.classes.measurement
Station = Base.classes.station

app = Flask(__name__)

@app.route("/")
def home_page():
    """List all available api routes"""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        #f"/api/v1.0/<start><br/>"
        #f"/api/v1.0/<start>/<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Returns JSON representation of dictionary of dates and precipitation data for the last 12 months from the last date datapoint in the database"""    
    
    session = Session(engine)

    # Query to retrieve the last 12 months of precipitation data
    last_12mo_precip = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    last_data_point = last_12mo_precip[0]

    # Calculating the date 1 year ago from the last data point in the database
    year_from_last_data_point = dt.datetime.strptime(last_data_point, "%Y-%m-%d") - dt.timedelta(days = 365)

    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= year_from_last_data_point).all()

    session.close()

    date_precip_dict = dict(results)

    return jsonify(date_precip_dict)

@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset"""

    session = Session(engine)

    # Query to retrieve stations names
    results = session.query(Measurement.station).group_by(Measurement.station).all()

    session.close()

    station_list = list(np.ravel(results))

    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    """Return a JSON list of temperature observations for latest year of data"""

    session = Session(engine)

    # Query to retrieve the last 12 months of precipitation data
    last_12mo_precip = session.query(Measurement.date).order_by(Measurement.date.desc()).first()

    last_data_point = last_12mo_precip[0]

    most_active_stations = session.query(Measurement.station, func.count(Measurement.station)).\
    group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()

    most_active = most_active_stations[0][0]

    # Calculating the date 1 year ago from the last data point in the database
    year_from_last_data_point = dt.datetime.strptime(last_data_point, "%Y-%m-%d") - dt.timedelta(days = 365)

    # Query to retrieve temperature observations for the last year, only for the most active station
    results = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= year_from_last_data_point).\
        filter((Measurement.station) == most_active).all()

    session.close()

    tobs_list = list(np.ravel(results))

    return jsonify(tobs_list)


#@app.route("/api/v1.0/<start>")
#def start():

#    session = Session(engine)

#    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
#        filter(Measurement.date >= start_date).all()

#    session.close()

#    temp_start_list = list(np.ravel(results))

#    return jsonify(temp_list)

#@app.route("/api/v1.0/<start>/<end>")
#def start_end(): 

#    session = Session(engine)

#    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).\
#        filter(Measurement.date >= start_date).\
#        filter(Measurement.date <= end_date).all()

#    session.close()

#    temp_start_end_list = list(np.ravel(results))

#    return jsonify(temp_start_end_list)

if __name__ == '__main__':
    app.run(debug = True)