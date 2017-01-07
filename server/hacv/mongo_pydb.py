from pymongo import MongoClient
from datetime import datetime

client = MongoClient()

countries = ['canada']
provinces = {'canada': ['ontario', 'british colombia', 'alberta'] }

db = client[countries[0]]
province = provinces[countries[0]][0]
collection = db[province]

result = collection.insert_one(
    {
        "address": {
            "street": "1265 Military Trail",
            "zipcode": "M1C 1A4",
            "coord": [-73.9557413, 40.7720266]
        },
        "date": datetime.today(),
    }
)
