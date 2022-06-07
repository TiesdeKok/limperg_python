### Imports
import re, sys, os, copy
import pandas as pd
import numpy as np

### Functions

def loadTest():
    """A function to evaluate whether the functions file succesfully loaded."""
    print("Functions are loaded.") 

def test_if_date(string):
    '''
    Test if a string is a date.

            Parameters:
                    string (string): The string that you want to test. 

            Returns:
                    is_date (bool): A True/False value indicating whether the string is a date.
    '''
    is_date = False
    try:
        date = pd.to_datetime(string)
        is_date = True
    except:
        pass
    return is_date     