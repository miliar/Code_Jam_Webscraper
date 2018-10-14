__author__ = 'barbapapa'
from collections import *
import pickle
import itertools as itt
import numpy as np
import math


def read_input(f_name):
    cases = []
    with open(f_name) as f:
        nr_cases = int(f.readline().strip())
        for c in range(nr_cases):
            P, Q = [int(x) for x in f.readline().strip().split('/')]
            cases.append((P, Q))
            pass
    return cases

def write_output(f_name, results):
    with open(f_name, 'w') as f:
        for i, r in enumerate(results):
            f.write('Case #'+str(i+1)+': '+r+'\n')

def is_power_of_2(num):
    rem = num
    while rem > 1:
        if rem % 2 == 0:
            rem //= 2
        else:
            return False
    return True


def solve_case(data):
    P, Q = data
    #assume no common factors
    if not is_power_of_2(Q):
        print 'impossible'
        return 'impossible'
    for i in range(1, 41):
        if P >= (Q//(2**i)):
            print i
            return str(i)


#file_name = 'A-test'
file_name = 'A-small-attempt0'
#file_name = 'A-large'
cases = read_input(file_name+'.in')
solution = [solve_case(x) for x in cases]
write_output(file_name+'.out', solution)
