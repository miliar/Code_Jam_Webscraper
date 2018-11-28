# python 3
import string
import itertools
import sys

def process_case(N, X, sizes):
    sizes.sort(reverse=True)
    disks = 0
    while True:
        if disks >= len(sizes):
            break
        if disks+1<len(sizes) and sizes[disks] + sizes[-1] <= X:
            sizes.pop()
        disks += 1
    return disks

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        N, X = line_of_numbers(next(lines))
        sizes = line_of_numbers(next(lines))
        result = process_case(N, X, sizes)
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
