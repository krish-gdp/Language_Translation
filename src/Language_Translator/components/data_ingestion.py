import os
import pandas as pd
import urllib.request as request
import zipfile
# from textsummarizer.logging import logger
from Language_Translator.logging import logger

from Language_Translator.utils.common import get_size

from pathlib import Path

from src.Language_Translator.constants import *


from src.Language_Translator.utils.common import read_yaml,create_directories


from src.Language_Translator.entity import (DataIngestionConfig)




class DataIngestion:
    def __init__(self, config:DataIngestionConfig):
        self.config= config

    def download_file(self):
        
        if not os.path.exists(self.config.local_data_file):

            df =pd.read_csv(self.config.source_URL,delimiter="\t",header=None)
            df = df[[0,1]]
            df.columns = ['English','French']
            df.to_csv(self.config.local_data_file)
            headers = df.columns
            logger.info("file  download!")
            
        else:

            logger.info("******File already exists******* ")



   