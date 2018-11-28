# python 3
import string
import itertools
import sys

def process_case(scounts):
    sum_counts = 0
    result = 0
    for s in range(len(scounts)):
        result = max(result, s-sum_counts)
        sum_counts += scounts[s]
    return result

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        n,scounts = next(lines).split()
        scounts = [int(x) for x in scounts]
        result = process_case(scounts)
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
    with open(infile, 'r') as f_in, open(outfile, 'w') as f_out:
        f_out.writelines(result_gen(input_gen(f_in)))

##start('A-test')
##start('A-small-attempt0')
start('A-large')
