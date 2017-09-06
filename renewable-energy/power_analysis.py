import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

data = pd.read_csv('data/power.csv')
time = data['t']
power = data['P']

slope, intercept, _, _, _ = stats.linregress(time, power)
t = np.linspace(np.min(time), np.max(time))
p = slope * t + intercept

time_range = np.max(time) - np.min(time)
power_range = np.max(power) - np.min(power)

plt.plot(time, power, 'bo', label='Mediciones')
plt.plot(t, p, 'r-', label='Regresión lineal')
plt.legend()

plt.title('Grafica de tendencia de la potencia')
plt.xlabel(r'$t$ [$s$]')
plt.ylabel(r'$P$ [W]')

text_x = np.min(time) + 0.1 * time_range
text_y = np.min(power) + 0.1 * power_range
line_eq = r'$P = {:.4f}t + {:.3f}$'.format(slope, intercept)
plt.text(text_x, text_y, line_eq)

plt.show()
