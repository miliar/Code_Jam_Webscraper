import string
import itertools
import sys

def process_case(N,K,B,T,X,V):
    if (K==0):
        return 0
    blockers = 0
    switches = 0
    done = 0
    i = N-1
    while (i>=0):
        if T * V[i] < (B-X[i]):
            blockers += 1
        else:
            switches += blockers
            done += 1
        if (done >= K):
            return switches
        i -= 1
    return 'IMPOSSIBLE'

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        N,K,B,T = line_of_numbers(next(lines))[:4]
        X = line_of_numbers(next(lines))[:N]
        V = line_of_numbers(next(lines))[:N]
        result = process_case(N,K,B,T,X,V)
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

#start('B-test')
start('B-large')
