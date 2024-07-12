import numpy as np
from matplotlib import pyplot as plt
import scipy
x=['$\\it{Quercus\ petraea}$','$\\it{Quercus\ robur}$','$\\it{Fraxinus\ excelsior}$',
'$\\it{Acer\ pseudoplatanus}$','$\\it{Castanea\ sativa}$','$\\it{Fagus\ sylvatica}$',
'$\\it{Quercus\ cerris}$','$\\it{Quercus\ rubra}$','$\\it{Tilia\ x\ europaea}$' ]
y=[4.755384615, 4.782647059, 5.4146875, 6.2478125, 3.749583333, 5.905142857, 4.807142857, 4.874, 5.452580645]
SE=[0.116512437, 0.08711284, 0.085941166, 0.108126209, 0.077694308,
0.060783915, 0.099969383, 0.065956696, 0.091625662]
43
plt.bar(x,y, width=0.70, color='c', edgecolor='black')
plt.ylim(3,7)
plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
plt.ylabel('Bark pH)
plt.errorbar(x,y,yerr=SE,color='k', fmt='o', markersize=3, capsize=4)
plt.gcf().subplots_adjust(bottom=0.4)
plt.gcf().subplots_adjust(top=0.9)
plt.show()
