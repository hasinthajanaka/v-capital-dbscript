from pymongo import MongoClient
import pandas as pd
import random

from pprint import pprint

client = MongoClient('mongodb://localhost:27017')
db = client.vcapital

data = pd.read_csv("us-500.csv")
print(data.dtypes)
print(db.list_collection_names())

users = []

for index, row in data[['first_name', 'last_name']].iterrows():
    user = {
        'firstname': row['first_name'],
        'lastname': row['last_name']
    }
    user_id = db.users.insert_one(user).inserted_id

    videos = [];

    for index in range(random.randrange(1, 15)):
        video = {
            'userid': user_id,
            'url': 'www.youtube.com'
        }
        videos.append(video)
    db.videos.insert_many(videos)
    print(row['first_name'], row['last_name'], videos)

