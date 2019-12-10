# explaination will be provided shortly
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

n_pts=100
np.random.seed(0)

""" top_region we have defined a variable which contain 100 points and disbributed randomly such that 
the point should be in the range 10,2 (x,y)  """
top_region=np.array([np.random.normal(10,2,n_pts), np.random.normal(12,2,n_pts)]).T
bottom_region= np.array([np.random.normal(5,2, n_pts), np.random.normal(6,2, n_pts)]).T

""""""
_, ax= plt.subplots(figsize=(4,4))

""" here we access the value of arrays and then we have drawn the points as in the plot with defined density  """
ax.scatter(top_region[:,0], top_region[:,1], color='r')
ax.scatter(bottom_region[:,0], bottom_region[:,1], color='b')

plt.show()
# print(top_region)
# print(bottom_region)


