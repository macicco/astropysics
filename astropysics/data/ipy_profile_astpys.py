""" 
The astropysics interactive IPython configuration file for ipython versions < .11
"""

import IPython.ipapi
#this is only necessary if ipythonrc isn't in use, so if it is, this import can be commented out
import ipy_defaults

ip = IPython.ipapi.get()

ip.ex("from __future__ import division")
ip.ex("import numpy")
ip.ex("import numpy as np")
ip.ex("from numpy import *")

ip.ex("import scipy")
ip.ex("from scipy import stats,optimize,ndimage,integrate,interpolate,special")

ip.ex("import pyfits")
try:
    ip.ex("import astropysics")
    #import typical modules
    ip.ex("from astropysics import phot,spec,coords,models,constants,objcat,obstools,io")
    try:
        ip.ex("from astropysics import gui")
    except ImportError:
        pass #this just means traits isn't installed
except ImportError:
    print "Unable to start astropysics profile, is astropysics installed?"
    



