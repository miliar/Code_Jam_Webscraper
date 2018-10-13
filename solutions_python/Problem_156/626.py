# python 3
import string
import itertools
import sys
import math

def process_case(p_counts):
    mp = max(p_counts)
    result = mp
    for max_per_person in range(1, 1+mp):
        num_operations = sum(math.ceil(pc/max_per_person)-1
                             for pc in p_counts)
        result = min(result, num_operations+max_per_person)
    return result

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        D = int(next(lines))
        p_counts = line_of_numbers(next(lines))
        result = process_case(p_counts)
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

##start('B-test')
##start('B-small-attempt0')
start('B-large')
