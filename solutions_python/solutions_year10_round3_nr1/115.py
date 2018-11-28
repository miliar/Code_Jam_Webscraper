import string
import itertools
import sys

def process_case(conn):
    result = 0
    for i in range(len(conn)):
        for j in range(i):
            if cross(conn[i],conn[j]):
                result += 1
    return result

def cross(a, b):
    if a[0]<b[0] and a[1]<b[1]:
        return False
    if a[0]>b[0] and a[1]>b[1]:
        return False
    return True
            
def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        N = int(next(lines))
        conn = [line_of_numbers(next(lines))[:2] for i in range(N)]
        result = process_case(conn)
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
