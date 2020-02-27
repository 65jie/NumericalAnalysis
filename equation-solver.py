from functools import partial
# import numpy as np


# solve equation with newton method
def newton(func, derFunc, initialValue, delta, epsilon, iterN):
    v = func(*[initialValue])
    print("k ", " x ", " f(x)")
    print(0, initialValue, v)
    if abs(v) < epsilon:
        return initialValue, v
    x0 = initialValue
    for i in range(0, iterN):
        x1 = x0 - v / derFunc(*[x0])
        v = func(*[x1])
        print(i + 1, x1, v)
        if abs(x1 - x0) < delta or abs(v) < epsilon:
            return x1, v
        else:
            x0 = x1
    return x1, v

# solve equation with bisection method
def bisection(func, a, b, delta, epsilon, iterN):
    mid = (a + b) * 0.5
    v = func(*[mid])
    print("k ", " x ", " f(x)")
    print(0, mid, v)
    if abs(v) < epsilon:
        return mid, v
    x0 = a
    x1 = b
    for i in range(0, iterN):
        f0 = func(*[x0])
        f1 = func(*[x1])
        if sign(f0) * sign(v) < 0:
            x1 = mid
        if sign(v) * sign(f1) < 0:
            x0 = mid
        mid = 0.5 * (x0 + x1)
        v = func(*[mid])
        print(i + 1, mid, v)
        if abs(x1 - x0) < delta or abs(v) < epsilon:
            return mid, v
    return mid, v

def sign(x):
    return -1 if x < 0 else 1 if x > 0 else 0

# a sum of a geometric progression with a1 = q = x
def sumFunc(sum, n, x):
    if x == 0 or x == 1:
        return n * x - sum
    return x * (1 - pow(x, n)) / (1 - x) - sum


# the derivative function of the sum function
def derFunc(n, x):
    if x == 0:
        return 1
    if x == 1:
        return (1 + n) * n / 2
    return (1 - (n + 1) * pow(x, n) + n * pow(x, n + 1)) / pow((1 - x), 2)


def main():
    n = 360
    sum = 75000 / 425.84
    iterN = 50
    initialValue = 0.5
    delta = 1e-6
    epsilon = 1e-12
    f = partial(sumFunc, sum, n)
    df = partial(derFunc, n)
    # newton(f, df, initialValue, delta, epsilon, iterN)
    bisection(f, 0, 1, epsilon, epsilon, 2 * iterN)


main()
