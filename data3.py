import pandas as pd
import numpy as num
import matplotlib.pyplot as plt

data = pd.read_csv('covid.csv')

data.plot(kind = 'scatter', x = 'date', y = 'cases',)

plt.show()