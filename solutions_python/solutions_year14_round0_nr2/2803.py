from math import floor
from sys import stdin, stdout


def time_in_k_steps(C, F, X, k):
    '''
    Assume that C < X!
    '''
    t = 0.0

    for j in range(k):
        t += C / R(F, j)
    
    t += X / R(F, k)
    return t


def R(F, k):
    return 2 + k*F


def optimal_steps(C, F, X):
    return max(0, int(floor( (X * F - 2 * C) / (C * F) )))


def optimal_time(C, F, X):
    k = optimal_steps(C, F, X)
    return time_in_k_steps(C, F, X, k)


if __name__ == '__main__':
    num_cases = int(stdin.readline().strip())
    for i in range(num_cases):
        data = stdin.readline().strip().split(" ")
        C, F, X = tuple([float(datum) for datum in data])
        stdout.write("Case #" + str(i + 1) + ": ")
        stdout.write(str(optimal_time(C, F, X)) + "\n")
