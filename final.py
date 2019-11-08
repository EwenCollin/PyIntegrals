import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from scipy.integrate import quad
import numpy as np


fig, ax = plt.subplots(1)



def element(f, ak, akp, *argsf):
    deltaX = math.fabs(akp - ak)
    if f == polynom:
        deltaY = f(argsf[0], argsf[1], argsf[2], ak)
    else:
        deltaY = f(ak)
    rect = patches.Rectangle((ak, 0), deltaX, deltaY, linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect)
    area = deltaX*deltaY
    return area

polynom = lambda a, b, c, x: x*x*a + x*b + x*c
squareRoot = lambda x: np.sqrt(x)
integrationSquareRoot = lambda i, j : (2/3)*math.pow(j, 3/2) - (2/3)*math.pow(i, 3/2)

def erreurSqrt(f, a, b, n):
    return math.fabs(integrationSquareRoot(a, b) - rectangle(f, a, b, n))

def rectangle(f, a, b, n, *argsf):
    totalArea = 0
    pas = (b - a)/n
    for x in range(int(n)):
        ak = x * pas + a
        akp = (x + 1) * pas + a
        if f == polynom:
            totalArea += element(f, ak, akp, argsf[0], argsf[1], argsf[2])
        else:
            totalArea += element(f, ak, akp)

    return totalArea

a = 1
b = 2
c = 3
i = 0
j = 10.0
n = 10
f = polynom

if f == squareRoot:
    print("Aire courbe racine carrée entre ", i, " et ", j, " avec ", n, " subdivisions", rectangle(squareRoot, i, j, n),
      " , valeur à trouver : ", integrationSquareRoot(i, j), " erreur de : ", quad(squareRoot, i, j)[0])

if f == polynom:
    print("Aire courbe polynome de degré 2 (a=", a, " b=", b, " c=", c, "entre ", i, " et ", j, " avec ", n, " subdivisions, on trouve : ",
      rectangle(f, i, j, n, a, b, c), " , valeur à trouver : ", quad(polynom, i, j, args=(a, b, c))[0])

x = np.linspace(0, 10, 1000)
if f == polynom:
    plt.plot(x, polynom(a, b, c, x), label='polynom')
if f == squareRoot:
    plt.plot(x, squareRoot(x), label='polynom')
plt.xlabel('x')
plt.ylabel('y')
axes = plt.gca()
axes.set_xlim([0, j])

if f == polynom:
    axes.set_ylim([0, polynom(a, b, c, j)])
if f == squareRoot:
    axes.set_ylim([0, squareRoot(j)])

plt.title("Intégrale")

plt.legend()

plt.show()