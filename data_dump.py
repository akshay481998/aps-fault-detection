import pymongo
import pandas as pd
import json
from sensor.config import mongo_client

DATA_FILE_PATH = "/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    #Convert dataframe to json so that we can dump these records into mongo db
    df.reset_index(drop=True,inplace=True) #inplace=True means this file will edit on same memory location

    json_records = list(json.loads(df.T.to_json()).values())
    print(json_records[0])

    #insert converted records into mongo db
    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)