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

### Set Up ### 
1. Navigate to the directory in which the `app.py` file lives on your local drive. 
2. Run the `app.py` program by typing `python app.py` directly into your terminal. 
3. Once running the program, several lines will print out in the terminal. Locate the line that begins with "Running on" followed by an `http://` link. 
4. Copy and paste that link into your browser. 
5. All possible routes are printed on the main pag which that link will take you directly to. 
6. To navigate to the different routes, simply copy and paste the whole route as is to the end of the link in the address bar. 
    - For both the start, and start/end routes you will have to provide a date between January 1, 2010 - August 23, 2017. 
    - The dates must be formatted as: `YYYY-MM-DD`. 
    - For start/end, the start date will go first and the end date will be second, separated by a backslash. 

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
  * Using a query from the [Station Analysis](#station-analysis) section to retrieve minimum, maximum and average temperatures, a filter is added to retrieve dates from a starting date provided by the user, to the end of the data set. 
* `/api/v1.0/<start>/<end>`
  * Using the same query as mentioned above, this route retrieves the minimum, maximum and average temperatures from a start date to an end date, both provided by the user. 

### Status ###

Project is: *in progress*

#### Contact 
Chloe Veras  
chloemveras@gmail.com  
[LinkedIn](https://www.linkedin.com/in/chloeveras/)
