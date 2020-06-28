
import numpy as np
from matplotlib import pyplot as plt
import matplotlib 

#x = ['1','2']
#y1 = [20, 26]
#y2 = [22, 23]

#plt.bar(x, y1, align =  'center', color =  'r') 
#plt.bar(x, y2, align =  'center', color =  'g')

#plt.title("two lines")
#plt.show()

from pylab import *
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
plt.plot(X,C, linewidth=2.5, linestyle="-", label="cosine")
plt.plot(X,S, linewidth=2.5, linestyle="-", label="sine")

legend(loc='upper left')

xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
       [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

yticks([-1, 0, +1],
       [r'$-1$', r'$0$', r'$+1$'])

ax = gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.show()