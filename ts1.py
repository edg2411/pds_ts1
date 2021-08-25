# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 15:57:30 2021

@author: Ezequiel Di Giulio
"""

import numpy as np

import matplotlib.pylab as plt

# x = np.linspace(-np.pi, np.pi, 201)
# plt.plot(x, np.sin(x))
# plt.xlabel('Angle [rad]')
# plt.ylabel('sin(x)')
# plt.axis('tight')
#plt.show()

amp=1
freq=1001
offset=np.pi
fs=1000
N=1000
ts=1/fs

tt = np.linspace(0, (N-1)*ts, N)

sin_sig = amp * np.sin(2*np.pi*freq*tt+offset)

plt.plot(tt, sin_sig)
plt.xlabel('Grilla temporal (tt)')
plt.ylabel('Amplitud sin_sig(tt)')
plt.axis('tight')
plt.show()