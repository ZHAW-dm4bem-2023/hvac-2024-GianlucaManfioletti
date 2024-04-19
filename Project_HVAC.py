import numpy as np
import pandas as pd
import psychro as psy

c = 1e3
l = 2496

#Model

A = np.zeros((8, 8))          # coefficents of unknowns
b = np.zeros(8)  

