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
            df =pd.read_csv(self.config.source_URL,delimiter="\t")
            df = df[[0,1]]
            df.columns = ['English','French']
            df.to_excel(self.config.local_data_file)
            headers = df.columns


            logger.info(f"file  download! with info: \n{headers}")

        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")



   