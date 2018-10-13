"""
    Oh yeah
"""
from sets import Set
import numpy as np

def get_proba(N,K,U,units):
    eps = 1e-8
    units = np.array(units)
    while U > eps and np.prod(units) < 1.-eps:
        min_unit = np.min(units)
        slice_mins = units[units <= min_unit+eps]
        mod_args = np.argsort(units)[:len(slice_mins)]
        if len(slice_mins) == N:
            second_smallest = 1.
        else:
            second_smallest = units[np.argsort(units)[len(slice_mins)]]
        if len(slice_mins) == 1:
            diff = second_smallest - min_unit
            increment = min(U, diff)
            U -= increment
            units[mod_args] += increment
        else:
            diff = second_smallest - min_unit
            increment = min(U, diff)
            U -= increment
            increment = increment / len(slice_mins)
            units[mod_args] += increment
        print('U : {}'.format(U))
    return np.prod(units)


with open('A-small.in') as file:
    with open('output.raw' ,'w') as ofile:
        n = int(file.readline())
        for i in range(1, n+1):
            N_K_l = file.readline()
            N = int(N_K_l.split(' ')[0])
            K = int(N_K_l.split(' ')[1])
            U = float(file.readline())
            units = file.readline().split(' ')
            units = [float(unit) for unit in units]
            ofile.write('Case #{}: {}\n'.format(i, get_proba(N,K,U,units)))
