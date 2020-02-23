##########################################################################################################################################
### GOOGLE ANALYTICS API QUERY TO PANDAS ###
##########################################################################################################################################

#api V3 setup
from google2pandas import *
import pandas as pd

#query parameters
max_result = 10000
store = 111111 #store number

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


##########################################################################################################################################
### USER CONFIGURATION ###
##########################################################################################################################################

conn = GoogleAnalyticsQuery(
        token_file_name='my_analytics.dat',
	secrets='my_client_secrets_v3.json')

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
