import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from scipy.integrate import quad
import numpy as np


fig, ax = plt.subplots(1)



def element(f, ak, akp, *argsf):
    deltaX = math.fabs(akp - ak)
    if f == polynom:
        deltaY = f(ak, argsf[0], argsf[1], argsf[2])
    else:
        deltaY = f(ak)
    rect = patches.Rectangle((ak, 0), deltaX, deltaY, linewidth=1, edgecolor='r', facecolor='none')
    #ax.add_patch(rect)
    area = deltaX*deltaY
    return area

def elementTrapeze(f, ak, akp, *argsf):
    deltaX = math.fabs(akp - ak)
    if f == polynom:
        deltaY = f(ak, argsf[0], argsf[1], argsf[2])
        deltaY2 = f(akp, argsf[0], argsf[1], argsf[2]) - deltaY
    else:
        deltaY = f(ak)
        deltaY2 = f(akp) - deltaY
    rect = patches.Rectangle((ak, 0), deltaX, deltaY, linewidth=1, edgecolor='r', facecolor='none')
    #ax.add_patch(rect)
    area = deltaX*deltaY + deltaX*deltaY2
    return area

polynom = lambda x, a, b, c: x*x*a + x*b + c
squareRoot = lambda x: np.sqrt(x)
integrationSquareRoot = lambda i, j : (2/3)*math.pow(j, 3/2) - (2/3)*math.pow(i, 3/2)

def approximation(f, a, b, n, *argsf):
    errorList = []
    for i in range(int(n)):
        errorList.append(erreur(f, a, b, i+1, argsf[0], argsf[1], argsf[2]))
    return errorList

def approximationTrapeze(f, a, b, n, *argsf):
    errorList = []
    for i in range(int(n)):
        errorList.append(erreurTrapeze(f, a, b, i+1, argsf[0], argsf[1], argsf[2]))
    return errorList

def erreur(f, a, b, n, *argsf):
    if f == polynom:
        return math.fabs(quad(f, a, b, args=(argsf[0], argsf[1], argsf[2]))[0] - rectangle(f, a, b, n, argsf[0], argsf[1], argsf[2]))
    else:
        return math.fabs(quad(f, a, b)[0] - rectangle(f, a, b, n))

def erreurTrapeze(f, a, b, n, *argsf):
    if f == polynom:
        return math.fabs(quad(f, a, b, args=(argsf[0], argsf[1], argsf[2]))[0] - trapeze(f, a, b, n, argsf[0], argsf[1], argsf[2]))
    else:
        return math.fabs(quad(f, a, b)[0] - trapeze(f, a, b, n))

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

def trapeze(f, a, b, n, *argsf):
    totalArea = 0
    pas = (b - a)/n
    for x in range(int(n)):
        ak = x * pas + a
        akp = (x + 1) * pas + a
        if f == polynom:
            totalArea += elementTrapeze(f, ak, akp, argsf[0], argsf[1], argsf[2])
        else:
            totalArea += elementTrapeze(f, ak, akp)

    return totalArea

a = 1
b = 0
c = 0
i = 0
j = 1.0
n = 1000
f = approximation
f2 = squareRoot

if f == squareRoot:
    print("Aire courbe racine carrée entre ", i, " et ", j, " avec ", n, " subdivisions", rectangle(squareRoot, i, j, n),
          " erreur de : ", erreur(f, i, j, n, a, b, c))

if f == polynom:
    print("Aire courbe polynome de degré 2 (a=", a, " b=", b, " c=", c, ") entre ", i, " et ", j, " avec ", n, " subdivisions, on trouve : ",
      trapeze(f, i, j, n, a, b, c), " , erreur de : ", erreur(f, i, j, n, a, b, c), ", valeur à trouver : ", quad(f, i, j, args=(a,b,c,))[0])

plt.xlabel('Nombre de subdivisions')
plt.ylabel('Erreur')
axes = plt.gca()
if f == polynom:
    x = np.linspace(0, 100, 1000)
    plt.plot(x, polynom(x, a, b, c), label='polynom')
    axes.set_ylim([0, polynom(j, a, b, c)])
    axes.set_xlim([0, j])
if f == squareRoot:
    x = np.linspace(0, 100, 1000)
    plt.plot(x, squareRoot(x), label='polynom')
    axes.set_xlim([0, j])
    axes.set_ylim([0, squareRoot(j)])
if f == approximation:
    x = np.arange(0, n)
    plt.loglog(x, approximation(squareRoot, i, j, n, a, b, c),label='Technique des rectangles')
    plt.loglog(x, approximationTrapeze(squareRoot, i, j, n, a, b, c),label='Technique des trapèzes')


plt.title("Erreur en fonction du nombre de subdivisions")

plt.legend()
plt.savefig('graphe.png')

plt.show()