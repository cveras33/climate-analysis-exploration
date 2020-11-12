# SQLAlchemy Homework - Surfs Up!

## Background ## 
A long holiday vacation in Honolulu, HI awaits and there is plenty of planning to do. To help with trip planning, some climate analysis on the area needs to be done. 

## Table of Contents ## 
* [Climate Analysis and Exploration](#climate-analysis-and-exploration)
  * [Precipitation Analysis](#precipitation-analysis)
  * [Station Analysis](#station-analysis)
* [Climate App](#climate-app)
* [Bonus: Other Recommended Analysis](#bonus-other-recommended-analysis)
  * [Temperature Analysis I](#temperature-analysis-i)
  * [Temperature Analysis II](#temperature-analysis-ii)
  * [Daily Temperature Average](#daily-temperature-average)
  
## Climate Analysis and Exploration ##
A basic climate analysis and data exploration of the climate database will be done using Python, and SQLAlchemy, ORM Queries, Pandas and Matplotlib. 

### Precipitation Analysis ### 
A query is designed to retrieve the `date` and `prcp` values from the past 12 months of precipitation data, based off the most recent date in the database. Based off the results of the query, the data retrieved is converted into a Pandas DataFrame and plotted, giving the results shown in the table below. 

![prcp_score_by_date](https://github.com/cveras33/sqlalchemy-challenge/blob/main/Images/prcp_score_by_date.png)

### Station Analysis ### 
Another query is designed to calculate the total number of stations, then a second query is designed to list all the stations with their corresponding observation count in descending order. Based off this query, it is determined that _USC00519281_ is the most active station. 

One more query is designed to retrieve the last 12 months of temperature observations for _USC00519281_ (the most active station). This data is then converted into a Pandas DataFrame and a histogram is plotted based on the data. The results are shown below. 

![tob_frequency](https://github.com/cveras33/sqlalchemy-challenge/blob/main/Images/tob_frequency.png)

## Climate App ## 
A Flask API is designed based on the queries that have just been developed for the initial analysis. 

#### Routes #### 
* `/`
 * The home page, which lists all other available routes.

* `/api/v1.0/precipitation`
 * Using the query from the [Precipitation Analysis](#precipitation-analysis) section, the query results are converted to a dictionary using `date` as the key and `prcp` as the value. 
 * The results are returned in a JSON representation of the dictionary. 

* `/api/v1.0/stations`
 * A JSON formated list of all the stations in the dataset is returned. 
 
* `/api/v1.0/tobs`
 * Using the query from the [Station Analysis](#station-analysis) section, the query results are converted to a list and all the temperature observations at the most active station for the last year are returned. 
 
* `/api/v1.0/<start>` 

* `/api/v1.0/<start>/<end>`

### Status ###

Project is: *in progress*

#### Contact 
Chloe Veras  
chloemveras@gmail.com  
[LinkedIn](https://www.linkedin.com/in/chloeveras/)
