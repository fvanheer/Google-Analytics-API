
# Query Google Analytics API

Simple and useful approach to include some Google Analytics data in your ETL process or enrich your data for analytics with google data. This boilerplate example will enable you to customise your queries to your business needs.   

* [Google API]() - More info
* [Google2Pandas](https://github.com/panalysis/Google2Pandas) - More info
* [Google Dimensions & Metrics Explorer](https://ga-dev-tools.appspot.com/dimensions-metrics-explorer/) - More info on dimensions and metrics that can be queried via the Google Analytics API

## Built With

* [Python 3.7](https://www.python.org/downloads/release/python-370/) - More information 

### Quick setup

```
pip install -r requirements.txt
```

or pip install 
```
google2pandas
pandas
```
### The Model

You can find the code in the google_query.py file

## Setup Guide

For this example, store your credentials anywhere you like and simply pass it through the query. You need to follow the [setup guide](https://developers.google.com/analytics/devguides/reporting/core/v3/quickstart/installed-py) to create the client_secrets_v3.json and analytics.dat files.

## Import the libraries

```Python

##########################################################################################################################################
### GOOGLE ANALYTICS API QUERY TO PANDAS ###
##########################################################################################################################################

#api V3 setup
from google2pandas import *
import pandas as pd

#query parameters
max_result = 10000 #max row results
store = 111111 #store number
```

## Define the google analytics queries

```Python
##########################################################################################################################################
### DEFINE QUERIES ###
##########################################################################################################################################

#query structure
query_new = {\
    'ids'           : store,
    'metrics'       : 'users',
    'dimensions'    : ['date', 'userType', 'browser'],
    'filters'       : 'userType==New Visitor',
    'start_date'    : '8daysAgo',
    'max_results'   : max_result}


query_returning = {\
    'ids'           : store,
    'metrics'       : 'users',
    'dimensions'    : ['date', 'userType', 'browser'],
    'filters'       : 'userType==Returning Visitor',
    'start_date'    : '8daysAgo',
    'max_results'   : max_result}
```

## Setup User Configuration

```Python
##########################################################################################################################################
### USER CONFIGURATION ###
##########################################################################################################################################

conn = GoogleAnalyticsQuery(
        token_file_name='my_analytics.dat',
	secrets='my_client_secrets_v3.json')
```

## Run the Query

```Python
##########################################################################################################################################
### DEFINE FUNCTION TO QUERY AND APPEND DATA ###
##########################################################################################################################################

#function to append all DF's to single table
def google_df():
    #write metadata to dataframes
    df_new, metadata = conn.execute_query(**query_new)
    df_returning, metadata = conn.execute_query(**query_returning)

    #append the dataframes
    df = df_new.append(df_returning, ignore_index=True)
    return(df)

# run the function
df_final = google_df()

# write to csv
df_final.to_csv('google_user_by_device.csv')
```

### Deployment Options
* Include the computations as a part of your ETL process (I use [KNIME](https://www.knime.com/))
* This can also be run as a simple cron job on a daily or weekly basis depending on the structure of the data and the use case. 

## Author

* **Francois van Heerden** - *Experience* - [LinkedIn Profile](https://www.linkedin.com/in/francois-van-heerden-9589825a/)

## Acknowledgments

* [Google2Pandas](https://github.com/panalysis/Google2Pandas) - More info

