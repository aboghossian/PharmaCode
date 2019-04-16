import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


c_init = [21.40661516,10.25530253,8.251885902,11.54955859,12.73909004,
          8.900023067,12.19931243,9.601998019,15.20290885,9.507726371,
          9.962021243,12.58318313,12.85919951,8.468153855,9.523436715,
          10.94560108,10.82514305,10.57433806,11.03924708,9.748863552,
          8.150771052,4.327826038,3.788296571,5.922770898,2.27167979,
          17.36664048,2.707867243,5.347175004,5.130618678,3.301411923,
          5.797104971,5.418052047,7.875976622,3.48179405,3.553321852,
          11.29895525,8.20532162,5.721022497,5.881667043,2.954485679]

kel = [5.110895625,2.834491842,2.487240488,3.072954449,3.300286641,
       2.596385072,3.196237228,2.718119183,3.791419919,2.701566293,
       2.781896959,3.270087777,3.323630111,2.523300981,2.704320515,
       2.960437634,2.938249749,2.892333874,2.977746296,2.744029608,
       2.018781557,1.624223067,1.568539312,1.788834128,1.412012335,
       2.969932964,1.457030367,1.72942803,1.707077686,1.518288924,
       1.7758644,1.736743108,1.990420575,1.536905802,1.544288043,
       2.343699337,2.024411612,1.76801208,1.784591882,1.482483362]

def deq(c, t):
    return -k * c

t = np.linspace(0, 2, 1000)

plt.figure()

for i, c0 in enumerate(c_init):
    k = kel[i]
    c = odeint(deq, c0, t)
    if i <20:
        plt.plot(t,c,'-m')
    else:
        plt.plot(t,c,'-c')

plt.title("BSA vs Flat Dosed Concentration Curve for Docetaxel")
plt.xlabel('Time')
plt.ylabel('Concentration')

custom_lines = [Line2D([0], [0], color='m', lw=4),
                Line2D([0], [0], color='c', lw=4)]

plt.legend(custom_lines, ['BSA', 'Flat-Dosed'],loc='upper right')

plt.show()
