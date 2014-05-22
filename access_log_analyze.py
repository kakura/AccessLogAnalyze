# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import json
from pandas import Series, DataFrame
from urlparse import urlparse,urlsplit

"""
AccessLog Analyze Class 
"""
__author__ = "s_kakura"
__version__ = "0.0.1"
__date__    = "15 April 2014"

class AccessLogAnalyze():

    def __init__(self, data_file,low_memory=False):
        self.original_data = pd.read_csv(data_file,low_memory=low_memory)
        #self.original_data = DataFrame.from_csv(data_file)
        
    def get_column(self,key):
        return self.original_data[key]
    
    def get_unique(self,key,querys=None):
        """Get unique items.

        Options:
        key -- key name
        query -- query(dict) example:{'id':'xxxx','time':'yyyymmdd'}
        """
        if querys is None:
            return self.original_data[key].dropna().unique()
        else:
            df = self.original_data
            for k,v in querys.items():
                df = self.mask(df,k,v)

            return df[key].dropna().unique()
                
    def mask(self,df,key,value):
        return df[df[key] == value]
     
    def extract(self,keys,querys=None):
        df = self.original_data
        if querys is not None:
            for k,v in querys.items():
                df = self.mask(df,k,v)
                
        return DataFrame(df,columns=keys)
        
