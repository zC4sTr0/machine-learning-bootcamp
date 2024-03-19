import numpy as np 
import matplotlib.pyplot as plt

t = np.linspace(0, 40, 1000)

dist_ladrao = 2.5 * t
dist_policial = 3 * (t-5)

fig, ax = plt.subplots()
plt.title('Distância entre o ladrão e o policial')
plt.xlabel('Tempo (s)')
plt.ylabel('Distância (km)')
ax.set_xlim(0, 40)
ax.set_ylim(0, 120)
ax.plot(t, dist_ladrao, c='green')
ax.plot(t, dist_policial, c='brown')
plt.axvline(x=30, color='red', linestyle='dashdot')
eixoy = plt.axhline(y=75, color='blue', linestyle='dashdot')
print(eixoy)
plt.show()