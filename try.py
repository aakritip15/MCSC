from sympy import *
import numpy as np
import matplotlib.pyplot as plt

# /usr/bin/python3
# /opt/homebrew/anaconda3/lib/python3.11/site-packages
x = np.array([0, 10, 15, 20, 22.5, 30])
y = np.array([0, 227.04, 362.78, 517.35, 602.97, 901.67])


data = [[i,j] for i,j in zip(x,y)]

points = np.array(data)

def qsi(data,x_new,plot=false):
    n = len(points) - 1

    x, y = symbols('x, y')
    a = symbols('a1:%d'%(n+1))
    b = symbols('b1:%d'%(n+1))
    c = symbols('c1:%d'%(n+1))

    f = [a[i]*x**2 + b[i]*x + c[i] - y for i in range(n)]


    equations = []
    equations.append(f[0].subs(x, points[0, 0]).subs(y, points[0, 1]))


    for i in range(n - 1):
        equations.append(f[i].subs(x, points[i + 1, 0]).subs(y, points[i + 1, 1]))
        equations.append(f[i + 1].subs(x, points[i + 1, 0]).subs(y, points[i + 1, 1]))

    equations.append(f[-1].subs(x, points[-1, 0]).subs(y, points[-1, 1]))


    # print(equations)
    fdx = [diff(fi, x) for fi in f]
    for i in range(n - 1):
        equations.append(fdx[i].subs(x, points[i + 1, 0]) - fdx[i + 1].subs(x, points[i + 1, 0]))



    equations.append(a[-1])
    print(equations)

    equation_tuple = tuple(equations)
    print(equation_tuple)

    coef_tuple = tuple(a+b+c)
    print(coef_tuple)

    solution = solve(equation_tuple, coef_tuple)
    print(solution)

    solved = solve(equations + [a[0]], a + b + c)

    if plot==true:
        for i in range(n):
            span = np.linspace(points[i, 0], points[i + 1, 0], 100)
            fi = f[i].subs(solved)
            if i == 0:
                plt.plot(span, [solve(fi.subs(x, i)) for i in span], 'r', label="a0 = 0")
            else:
                plt.plot(span, [solve(fi.subs(x, i)) for i in span], 'r')
        plt.scatter(points[:, 0], points[:, 1])
        plt.grid()
        plt.legend()
        plt.show()

    for i in range(n):
        if (points[i,0]) <= x_new >= (points[i,0]):
            print("1")
            fi = f[i].subs(solved)
            yn= solve(fi.subs(x,x_new))
        else:
            print("2")
            yn = 0

    return yn

y_new = qsi(data,16,plot=true)
print(yn)