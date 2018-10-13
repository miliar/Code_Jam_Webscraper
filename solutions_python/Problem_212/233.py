from copy import deepcopy
from collections import namedtuple
import functools
import numpy as np
import common 
from common import *


def parse(lines):
    N, P = lines.next().split()
    N, P = int(N), int(P)
    arr = [int(x) for x in lines.next().split()]
    return P, arr


####

def pair_off(mods, P):
    mods = sorted(mods)
    n = mods[0]

    if n == 0:
        return mods[1:]
    
    if P - n in mods:
        return 
    if 0 in mods:
        return

# def solve(input):
#     P, groups = input
#     groups = np.array(sorted([x % P for x in groups]))
#     zeros = np.where(groups == 0)
    
#     groups2 = [x for x in groups if x != 0]
#     groups3 = [(a + b) % P for a,b in zip(groups2,groups2[::-1])]
#     zeros = len(groups) - len(groups2)
#     zeros += len([x for x in groups3 if x == 0])
#     return zeros

def solve(input):
    P, groups = input
    groups = list(groups)
    happy = 0
    mods = sorted([g % P for g in groups])

    while mods:
        if mods[0] == 0:
            happy += 1
            mods.remove(0)
            continue
        if mods[0] == 1:
            if 2 in mods:
                mods.remove(1)
                mods.remove(2)
                happy += 1
                continue
        break
    # first is always happy
    leftover = 0
    for m in mods:
        if leftover == 0:
            happy += 1
        leftover = (leftover + (P - m)) % P
    happy
    return happy

####

output_newline = False


def write(x):
    return write_cases(x, newline=output_newline)


def test(input=None, output=None):
    input = input or example_input
    output = output or example_output
    a_test = make_test(parse, solve, write)
    a_test(input, output)
    print 'ok'


def run(f):
    inputs = read_by_parser(f, parse)
    f2 = f + '.out'
    outputs = [format(solve(cake)) for cake in inputs]
    save_cases(f2, outputs, newline=output_newline)
    return outputs
    

##### 

example_input = \
"""3
4 3
4 5 6 4
4 2
4 5 6 4
3 3
1 1 1
"""

example_output = \
"""Case #1: 3
Case #2: 4
Case #3: 1
"""
