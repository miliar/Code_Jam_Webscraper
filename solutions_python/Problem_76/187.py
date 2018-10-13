# python 3
import string
import itertools
import sys

def process_case(data):
    mask = 0
    for num in data:
        mask = mask ^ num
    if mask == 0:
        result = sum(data) - min(data)
    else:
        result = -1
    return result

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        n = int(next(lines))
        s = next(lines)
        data = [int(x) for x in s.split()]
        result = process_case(data)
        if result == -1:
            result = 'NO'
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

##start('C-test')
##start('C-small-attempt0')
start('C-large')
