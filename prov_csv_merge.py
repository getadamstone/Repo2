#join the csv files
import pandas as pd
import numpy
import os
#pd.set.option('display.max_columns', 500)
#pd.set.option('display.width', 1000)

Base_Provider_Enrollment_File_df = pd.read_csv('/Users/aston/PyScript/cms_prov_data/Base_Provider_Enrollment_File.csv',encoding = 'latin')
Addy_Provider_Enrollment_File_df = pd.read_csv('/Users/aston/PyScript/cms_prov_data/Address_Provider_Enrollment_File.csv',encoding = 'latin')

if os.path.exists('/Users/aston/PyScript/cms_prov_data/cms_prov_data_combined.csv'):
  os.remove('/Users/aston/PyScript/cms_prov_data/cms_prov_data_combined.csv')
else:
  print('File does not exists')

#len(Base_Provider_Enrollment_File_df)
prov_addy_combined = pd.merge(Base_Provider_Enrollment_File_df,Addy_Provider_Enrollment_File_df, left_on='ENRLMT_ID', right_on ='ENRLMT_ID', how='right')
prov_addy_combined.to_csv('/Users/aston/PyScript/cms_prov_data/cms_prov_data_combined.csv',index=False)
