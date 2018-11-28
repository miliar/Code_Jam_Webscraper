from codejam import *

def read_file(f):
    return read_int_list(f)

def solver(case):
    x, r, c = case
    total = r*c
    if total % x:
        #print('RICHARD')
        return 'RICHARD'
    if r < x and c < x:
        #print('RICHARD')
        return 'RICHARD'
    if r < x-1 or c < x-1:
        #print('RICHARD')
        return 'RICHARD'
    #print('GABRIEL')
    return 'GABRIEL'


solve('D-small-attempt0', read_file, solver)
