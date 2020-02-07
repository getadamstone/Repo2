#download the prov csv
import urllib.request

#This file is a point in time snapshot of enrollment level data for providers actively enrolled in Medicare.
prov_base = 'https://data.cms.gov/api/views/ykfi-ffzq/rows.csv?accessType=DOWNLOAD&bom=true&format=true'
#This file is a point in time snapshot of select practice location information for active enrollments
prov_addy = 'https://data.cms.gov/api/views/je57-c47h/rows.csv?accessType=DOWNLOAD&bom=true&format=true'

#get files and write to project folder/Users/aston/PyScript/cms_prov_data/
urllib.request.urlretrieve(prov_base, '/Users/aston/PyScript/cms_prov_data/Base_Provider_Enrollment_File.csv')
urllib.request.urlretrieve(prov_addy, '/Users/aston/PyScript/cms_prov_data/Address_Provider_Enrollment_File.csv')
