import scipy.integrate
from scipy import integrate
import math
import cmath
import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6]
y = [i ** 2 for i in range(1, 7)]
fig = plt.figure("fff")
plt.plot(x, np.sin(x),"g--")
plt.plot(x, y)

plt.show()

# w = 1
# x = complex(1, 2)
#  print(x, x.real)
# f = lambda x: cmath.sin(x) * cmath.exp(-1 * x * w)
#
# print(f)
#
# integrel = scipy.integrate.quad(f, 0, 1)
# print(integrel)
