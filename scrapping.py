# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:47:56 2019

@author: Ilmarsl
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
from IPython.display import display

newUrl ='https://www.ss.com/lv/real-estate/plots-and-lands/riga-region/marupes-pag/'
dftables = pd.read_html(newUrl)
marupes = dftables[8]
different_cols = ['none2', 'none2', 'Sludinājuma datums', 'Ciems' 'Cena m2', 'Cena']
#marupes = marupes.loc[:, different_cols]
marupes.head()
print(marupes)