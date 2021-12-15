import requests
import json

#url ='https://www.brewersassociation.org/directories/breweries/'

res = requests.get('https://www.brewersassociation.org/wp-content/themes/ba2019/json-store/breweries/breweries.json?nocache=1639528237993')

data = json.loads(res.json())

#dict keys
# data.keys()

# checking type
# type(data['ResultData'][0])

# grabing 1st index keys
# data['ResultData'][0].keys()

#grabing data from first index
# data['ResultData'][0]

import pandas as pd

# Creating DataFrame
df = pd.DataFrame(data)

# df.head()

df = pd.DataFrame(data['ResultData'])

#data.head()

# checking num of rolls and columns
# df.shape

# storing to CSV file
df.to_csv('beer.csv', index=False)



