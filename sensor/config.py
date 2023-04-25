import pymongo
import pandas as pd
import json
from dataclasses import dataclass
import os

@dataclass
class EnvironmentVariable:
    mongo_db_url:str = os.getenv("MONGO_DB_URL")

env_var = EnvironmentVariable()

# Provide the mongodb localhost url to connect python to mongodb.
mongo_client = pymongo.MongoClient(env_var.mongo_db_url)

TARGET_COLUMN="class"
