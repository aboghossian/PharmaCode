import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import seaborn as sns

sns.set()

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


c0_bsa = np.mean(c_init[:20])
kel_bsa = np.mean(kel[:20])

c0_flat = np.mean(c_init[20:])
kel_flat = np.mean(kel[20:])

t = np.linspace(0, 2, 1000)

def deq_bsa(c, t):
    return -kel_bsa * c

def deq_flat(c, t):
    return -kel_flat * c

c_bsa = odeint(deq_bsa, c0_bsa, t)
c_flat = odeint(deq_flat, c0_flat, t)

plt.title("Average Patient Concentration Curve (BSA and Flat Dosed) for Docetaxel")
plt.xlabel('Time (hr)')
plt.ylabel('Concentration (mg/L)')

plt.plot(t,c_bsa,'-b')
plt.plot(t,c_flat,'-r')

custom_lines = [Line2D([0], [0], color='b', lw=4),
                Line2D([0], [0], color='r', lw=4)]
plt.legend(custom_lines, ['BSA', 'Flat-Dosed'],loc='upper right')

plt.show()
