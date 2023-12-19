import numpy as np
import matplotlib.pyplot as plt
import os
import re

Dirs = ['Mask/','NoMask/'] #Whether or not I have used a mask function for computing ionisation channels
ions = 'td.general/ion_ch'
laser = 'td.general/laser'


"""

Just a bit of house keeping seeing as my jupyter kernel doesn't want to load in...

"""
if __name__ == "__main__":
    Debug = True

if Debug == True:
    print(os.getcwd())

omega = 0.057 #This corresponds to around 800nm driving field
specs = {"mask": np.loadtxt('Mask/hs-mult.x'), "nomask": np.loadtxt('NoMask/hs-mult.x')}
las = {"mask": np.loadtxt('Mask/'+laser), "nomask": np.loadtxt('NoMask/'+laser)}

fig, axs = plt.subplots(nrows=2, ncols = 2)
fig.subplots_adjust(hspace=0,wspace=0)
axs = axs.flatten()
axs[0].plot(specs['mask'][:,0]/omega, np.log10(specs['mask'][:,1]), color = 'k', label = 'Mask Harmonics')
axs[2].plot(specs['nomask'][:,0]/omega, np.log10(specs['nomask'][:,1]), color = 'g', label = 'No Mask Harmnics')
axs[1].plot(las['mask'][:,1], las['mask'][:,2], color = 'k', linestyle = 'dashed', label = 'Mask Laser')
axs[3].plot(las['nomask'][:,1], las['nomask'][:,2], color = 'g', linestyle = 'dashed', label = 'No Mask Laser')
fig.legend(ncol = 2, mode = 'expand')
plt.show()