# python 3
import string
import itertools
import sys

def process_case(tab):
    result = 0
    for i in range(len(tab)):
        if tab[i] != i+1:
            result += 1
    return result

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        n = int(next(lines))
        data = next(lines)
        tab = [int(x) for x in data.split()]
        result = process_case(tab)
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

##start('D-test')
##start('D-small-attempt0')
start('D-large')
