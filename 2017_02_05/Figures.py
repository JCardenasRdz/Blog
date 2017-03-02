import matplotlib.pyplot as plt
import numpy as np

def T2decay(decay_rate = 1/0.020 , xdata = np.linspace(0,.10,50)):
    return np.exp(-decay_rate * xdata)

# Create data set
decay_times = np.linspace(.050,100,10)
Ydata=np.zeros(50,10)

for  idx, time in enumerate(L):
    S= T2decay(1/decay_times[0])





plt.plot(S_clean); plt.xlabel('X data'); plt.ylabel('Y data')
plt.show();
