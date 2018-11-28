# python 3
import string
import itertools
import sys

def count_overlapping(s, sub):
    cnt = 0
    idx = 0
    while(True):
        idx = s.find(sub, idx) + 1
        if idx > 0:
            cnt += 1
        else:
            return cnt

def process_case(keys, expected, S):
    maxval = 0
    sumval = 0
    for tseq in itertools.product(keys, repeat=S):
        seq = ''.join(tseq)
        cnt = count_overlapping(seq, expected)
        maxval = max(maxval, cnt)
        sumval += cnt
    avg = sumval / (len(keys)**S)
    result = maxval - avg
    return result

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        K,L,S = line_of_numbers(next(lines))
        keys = next(lines)
        expected = next(lines)
        result = process_case(keys, expected, S)
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
start('B-small-attempt0')
##start('B-large')
