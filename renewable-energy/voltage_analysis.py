import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_csv('data/voltage.csv')
time = data['t']
voltage = data['V']

slope, intercept, _, _, _ = stats.linregress(time, voltage)
t = np.linspace(np.min(time), np.max(time))
v = slope * t + intercept

time_range = np.max(time) - np.min(time)
voltage_range = np.max(voltage) - np.min(voltage)

plt.plot(time, voltage, 'bo', label='Mediciones')
plt.plot(t, v, 'r-', label='Regresión lineal')
plt.legend()

plt.title('Grafica de tendencia del voltaje')
plt.xlabel(r'$t$ [$s$]')
plt.ylabel(r'$V$ [V]')

text_x = np.min(time) + 0.1 * time_range
text_y = np.min(voltage) + 0.1 * voltage_range
line_eq = r'$V = {:.3f}t + {:.3f}$'.format(slope, intercept)
plt.text(text_x, text_y, line_eq)

plt.show()
