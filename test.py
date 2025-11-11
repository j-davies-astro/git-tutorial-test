import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,100)

y = x**2 + x + 1943859374958375

s = "blah bhlahosueifoisn"



plt.figure()

plt.plot(x,y)

plt.savefig('blah')

plt.show()