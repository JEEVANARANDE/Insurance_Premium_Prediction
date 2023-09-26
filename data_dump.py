import pymongo
import json
import pandas as pd
import urllib.parse

username = 'jeevanarande'
#password = 'Datascience@93'


password = urllib.parse.quote("Datascience@93")

client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.yvzltge.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = (r"C:\jeevan\Insurance_Premium_Prediction\Insurance_Premium_Prediction\insurance.csv")

DATABASE_NAME = "INSURANCE"

COLLECTION_NAME = "INSURANCE_PROJECT"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns : {df.shape}")
    df.reset_index(drop = True, inplace = True)
    json_record = list(json.loads(df.T.to_json()).values())
    
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)