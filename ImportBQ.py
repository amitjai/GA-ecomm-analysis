#%%
## Libraries
import numpy as np
import pandas as pd 
import pandasql as ps
import plotly as plt
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas_gbq


#%% Variables

#Define variables to import GCP projects 
gcp_project = 'ga-bq-analysis'
#bq_dataset = 'bigquery-public-data'
bq_dataset = 'ga_ecomm_july2016'

#Define variables for importing local dataset
file_master = 'dataset.xlsx'
dir_processed = '2_processed'
sheets = ['dataset']

#%%Connections 

# define gcp credentials and BQ client
credentials = service_account.Credentials.from_service_account_file(r'C:\Users\ajyog\Downloads\ga-bq-analysis-6b48f2446f2c.json'
)
client = bigquery.Client(credentials = credentials, project = gcp_project)
dataset_ref = client.dataset(bq_dataset, project=gcp_project)

#%% Function for Standard Query to pandas Dataframe 
def gcp2df(sql):
    query = client.query(sql)
    results = query.result()
    return results.to_dataframe()

# %%
# Input your Query Syntax here; You may try it first at https://console.cloud.google.com/bigquery
# Example Query 
QUERY = (
    'SELECT * FROM `bigquery-public-data.covid19_nyt.us_counties` ' 
    'ORDER BY date DESC,confirmed_cases DESC '
    'LIMIT 20')
df = gcp2df(QUERY)




#%%
query_job = client.query(QUERY)    # Start Query API Request
query_result = query_job.result()  # Get Query Result
df = query_result.to_dataframe()   # Save the Query Resultto Dataframe

#%% Function to Read local data files 
print(f'Reading Master data from: {file_master}')
for sheet in sheets:
    print(f'> {sheet}...')
    #### UN-COMMENT THE EXEC LINE BELOW WHEN YOU WANT TO READ THE DATA
    exec(f'tbl_{sheet} = pd.read_excel(file_master, sheet_name="{sheet}")')
    