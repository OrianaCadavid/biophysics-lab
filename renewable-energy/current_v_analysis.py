import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_csv('data/current_v.csv')
time = data['t']
current = data['I']

slope, intercept, _, _, _ = stats.linregress(time, current)
t = np.linspace(np.min(time), np.max(time))
i = slope * t + intercept

time_range = np.max(time) - np.min(time)
current_range = np.max(current) - np.min(current)

plt.plot(time, current, 'bo', label='Mediciones')
plt.plot(t, i, 'r-', label='Regresión lineal')
plt.legend()

plt.title('Grafica de tendencia de la corriente')
plt.xlabel(r'$t$ [$s$]')
plt.ylabel(r'$I$ [A]')

text_x = np.min(time) + 0.1 * time_range
text_y = np.min(current) + 0.1 * current_range
line_eq = r'$I = {:.4f}t + {:.3f}$'.format(slope, intercept)
plt.text(text_x, text_y, line_eq)

plt.show()
