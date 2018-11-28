# python 3
import string
import itertools
import sys

def process_case(data):
    n = len(data)
    tab = n * [-1]
    tab[0] = data[0][0]
    for i in range(n):
        if tab[i] < 0:
            continue
        d = data[i][0]
        h = tab[i]
        for j in range(i+1,n):
            dj,lj = data[j]
            if dj > d + h:
                break
            hj = min(lj, dj-d)
            tab[j] = max(tab[j], hj)
    return 'YES' if tab[n-1]>=0 else 'NO'

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        ndata = int(next(lines))
        data = list()
        for i in range(ndata):
            data.append(tuple(line_of_numbers(next(lines))))
        D = int(next(lines))
        data.append((D,0))
        result = process_case(data)
        yield 'Case #{0}: {1}\n'.format(ci, result)
    
def line_of_numbers(s):
    return [int(sub) for sub in s.split()]

def input_gen(f_in):
    for line in f_in:
        if line.endswith('\n'):
            line = line[:-1]
        yield line

def start(basename):
    infile = basename + '.in'
    outfile = basename + '.out'
    f_in = open(infile, 'r')
    f_out = open(outfile, 'w')
    f_out.writelines(result_gen(input_gen(f_in)))
    f_in.close()
    f_out.close()

##start('A-test')
##start('A-small-attempt0')
start('A-large')
