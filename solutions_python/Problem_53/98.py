import string
import itertools
import sys

def process_case(n,k):
    bits = (1<<n)-1
    if (bits & k) == bits:
        return 'ON'
    else:
        return 'OFF'

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        n,k = line_of_numbers(next(lines))[:2]
        result = process_case(n,k)
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

start('A-test')
