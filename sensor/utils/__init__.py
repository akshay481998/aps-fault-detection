import pandas as pd 
from sensor.logger import logging
from sensor.exception import SensorException
import os,sys
from sensor.config import mongo_client


def get_collection_as_dataframe(database_name:str,collection_name:str)->pd.DataFrame:
    """
    Description: This function returns collection as dataframe
    =============================================
    params:
    database_name : database name
    collection_name: collection name
    =============================================
    return Pandas dataframe as collection
    """
    try:
        logging.info(f"Reading data from database: {database_name} and collection: {collection_name}")
        df = pd.DataFrame(list(mongo_client[database_name][collection_name].find()))
        logging.info(f"Found columns: {df.columns}")
        if "_id" in df.columns:
            logging.info("Dropping column: _id")
            df = df.drop('_id',axis=1)
        logging.info(f"Rows and columns in df: {df.shape}")
        return df
    except Exception as e:
        raise SensorException(e,sys)

