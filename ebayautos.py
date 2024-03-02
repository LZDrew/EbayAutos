# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

ebayauto = pd.read_csv("/Users/drew/Documents/Python/Data_Analysis/Ebay_car/autos.csv", encoding="Latin-1")
print(ebayauto.info())