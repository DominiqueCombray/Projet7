# ====================
#
# Exploratory Daya Analysis
#
# Basé sur le Kernel Kaggle "https://www.kaggle.com/code/willkoehrsen/start-here-a-gentle-introduction/notebook"
#
# ====================


# numpy and pandas for data manipulation
import numpy as np
import pandas as pd

# sklearn preprocessing for dealing with categorical variables
from sklearn.preprocessing import LabelEncoder

# File system manangement
import os

# Suppress warnings
import warnings

warnings.filterwarnings("ignore")

# matplotlib and seaborn for plotting
import matplotlib.pyplot as plt
import seaborn as sns

# List files available
print(os.listdir("./input/"))
