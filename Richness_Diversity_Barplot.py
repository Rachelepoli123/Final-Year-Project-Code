import numpy as np
from matplotlib import pyplot as plt
import scipy
x=['$\\it{Quercus\ petraea}$','$\\it{Quercus\ robur}$','$\\it{Fraxinus\ excelsior}$',
'$\\it{Acer\ pseudoplatanus}$','$\\it{Castanea\ sativa}$','$\\it{Fagus\ sylvatica}$',
'$\\it{Quercus\ cerris}$','$\\it{Quercus\ rubra}$','$\\it{Tilia\ x\ europaea}$' ]
Richness = [17, 29, 43, 34, 21, 33, 24, 25, 32]
Diversity = [46, 166, 251, 195, 90, 220, 70, 73,194]
width=0.4
values=np.arange(len(x))
plt.bar(values,Richness, width, label='Richness', color='g', edgecolor='black')
plt.bar(values+width,Diversity, width, label='Diversity', color='yellowgreen', edgecolor='black')
plt.ylim(0.1,275)
plt.xticks(values+0.2, x, rotation=45, ha='right', rotation_mode='anchor')
plt.ylabel('Bryophyte Count')
plt.legend()
plt.gcf().subplots_adjust(bottom=0.4)
plt.gcf().subplots_adjust(top=0.9)
plt.grid(zorder=0)
plt.gca().set_axisbelow(True)
plt.show()
