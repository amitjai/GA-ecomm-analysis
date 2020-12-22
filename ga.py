#%%
## Libraries
import numpy as np
import pandas as pd 
import pandasql as ps
import plotly


#%%
## Functions
export_table = lambda dataframe, filename: dataframe.to_excel(filename, index=False)


## Variables
file_master = 'dataset.xlsx'
dir_processed = '2_processed'
sheets = ['dataset']

#%%
# Read all data files
print(f'Reading Master data from: {file_master}')
for sheet in sheets:
    print(f'> {sheet}...')
    #### UN-COMMENT THE EXEC LINE BELOW WHEN YOU WANT TO READ THE DATA
    exec(f'tbl_{sheet} = pd.read_excel(file_master, sheet_name="{sheet}")')


Test = 1 

