import matplotlib.pyplot as plt
from scipy import random
import numpy as np

a = 0
b = (np.pi) / 2 # limit of integration
N = 500

def fun(x):
    return np.sin(x)

# answer = (b-a)/float(N) * integral
areas = []

for i in range(N):
    xrand = np.zeros(N)
    for i in range(len(xrand)):
        xrand[i] = random.uniform(a, b)

    integral = 0
    for i in range(N):
        integral += fun(xrand[i])  # adding function evaluation
    answer = (b - a) / float(N) * integral
    areas.append(answer)

plt.title("Distribution of areas calculated")
plt.hist(areas,bins=30, ec = 'black')
plt.xlabel("Area")
plt.show()