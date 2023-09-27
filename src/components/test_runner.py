import os
import sys

from src.logger import logging
from src.exception import CustomException

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

try:

    if __name__=="__main__":

        data_injestion=DataIngestion()
        train_data_path,test_data_path=data_injestion.initiate_data_ingestion()

        data_transformation=DataTransformation()
        train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data_path,test_data_path)

        model_trainer =ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_arr,test_arr))

except Exception as e:
    raise CustomException(e,sys)






