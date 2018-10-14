from copy import deepcopy
from collections import namedtuple
import functools
import numpy as np
import common 
from common import read_input, write_cases, save_cases

def run(f):
    inputs = parse_input(open(f).read())
    f2 = f + '.out'
    outputs = []
    for cake in inputs:
        outputs += ['\n' + format(cut(cake))]
    save_cases(f2, outputs)
    
def parse_input(txt):
    lines = iter([x for x in txt.split('\n') if x])
    T = int(lines.next())
    inputs = []
    for line in lines:
        N, P = line.split() 
        N, P = int(N), int(P)

        arr = []
        for _ in range(N):
            line = lines.next()
            arr += [[x for x in line.strip()]]
        inputs += [np.array(arr)]
    return inputs


def cut(cake):
    cake = cake.copy()
    mask = cake == '?'
    fill_em = np.where(mask.any(axis=1))[0]
    [fill(cake[i]) for i in fill_em]
    dupe_rows(cake)
    return cake

def format(cake):
    return '\n'.join(''.join(r) for r in cake)

def fill(row):
    ix = np.where(row != '?')[0]
    if ix.size == 0:
        return
    last = 0
    for i in ix:
        row[last:i+1] = row[i]
        last = i + 1
    row[i:] = row[i]
    

def dupe_rows(cake):
    mask = cake != '?'
    ix = np.where(mask.all(axis=1))[0]
    if ix.size == 0:
        return
    last = 0
    for i in ix:
        cake[last:i+1] = cake[i]
        last = i + 1
    cake[i:] = cake[i]
    



##### 

example_input = \
"""3
3 3
G??
?C?
??J
3 4
CODE
????
?JAM
2 2
CA
KE
"""

example_output = \
"""Case #1:
GGJ
CCJ
CCJ
Case #2:
CODE
COAE
JJAM
Case #3:
CA
KE
"""

