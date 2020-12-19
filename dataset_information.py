import numpy as np
import pandas as pd
import pandas_profiling
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

class Dataset_inspection:
    
    def __init__(self,data):
        self.data=data
        
    def dataset_info(self):
        print('\nShape of Dataset',self.data.shape)
        print('\nNumber of Rows',self.data.shape[0],'\nNumber of Columns: ',self.data.shape[1])
        print('\nFeature Names : \n',self.data.columns.values)
        print('\nInformation about Datatypes: ')
        print('\n%s'%self.data.info())
        print('\nUnique values per column: \n%s'%self.data.nunique())
        print('\nAny Missing Values in data?: %s'%self.data.isnull().values.any())
    
    

