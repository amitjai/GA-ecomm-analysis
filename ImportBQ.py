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
gcp_project = 'ga-bq-analysis'
#bq_dataset = 'bigquery-public-data'
bq_dataset = 'ga_ecomm_july2016'


file_master = 'dataset.xlsx'
dir_processed = '2_processed'
sheets = ['dataset']


#%%Connections 

credentials = service_account.Credentials.from_service_account_file(r'C:\Users\ajyog\Downloads\ga-bq-analysis-6b48f2446f2c.json'
)
client = bigquery.Client(credentials = credentials, project = gcp_project)
dataset_ref = client.dataset(bq_dataset, project=gcp_project)

# %%
df.head()
# %%
df.head()
# %%
df.head()
#%% Credentials 
credentials = service_account.Credentials.from_service_account_file(
    'C:\Users\ajyog\Downloads\ga-bq-analysis-6b48f2446f2c.json' ,
     scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

#client = bigquery.Client(credentials=credentials, project=gcp_project,)

#df = pandas_gbq.read_gbq(sql, project_id="YOUR-PROJECT-ID", credentials=credentials)

# %% Functions 

def gcp2df(sql):
    query = client.query(sql)
    results = query.result()
    return results.to_dataframe()

    

# %%
# Input your Query Syntax here; You may try it first at https://console.cloud.google.com/bigquery
QUERY = (
    'SELECT * FROM `bigquery-public-data.covid19_nyt.us_counties` ' 
    'ORDER BY date DESC,confirmed_cases DESC '
    'LIMIT 20')

df = gcp2df(QUERY)




#%%
query_job = client.query(QUERY)    # Start Query API Request
query_result = query_job.result()  # Get Query Result
df = query_result.to_dataframe()   # Save the Query Resultto Dataframe

# %%

