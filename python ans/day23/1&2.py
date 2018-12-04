import pandas as pd
import numpy as np

int_ary = np.arange(1,17).reshape(4,4)

masked = np.ma.masked_array(int_ary,mask=int_ary%3==0)
print masked