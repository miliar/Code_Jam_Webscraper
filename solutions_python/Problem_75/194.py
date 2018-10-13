# python 3
import string
import itertools
import sys

def prep_comb(comb):
    ncomb = {}
    for x in comb:
        a,b,c = x
        ncomb[a+b] = c
        ncomb[b+a] = c
    return ncomb

def prep_opp(opp):
    d = {}
    for x in opp:
        a,b = x
        if a not in d:
            d[a] = set()
        d[a].add(b)
        if b not in d:
            d[b] = set()
        d[b].add(a)
    return d

def process_case(comb, opp, seq):
    result = ''
    for item in seq:
        result = result + item
        while len(result) >= 2:
            key = result[-2:]
            if key in comb:
                result = result[:-2] + comb[key]
            else:
                break
        if len(result) >= 1:
            key = result[-1]
            if key in opp:
                if opp[key] & set(result):
                    result = ''
    return result

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        s = next(lines)
        gen = (x for x in s.split())
        numComb = int(next(gen))
        comb = [next(gen) for i in range(numComb)]
        numOpp = int(next(gen))
        opp = [next(gen) for i in range(numOpp)]
        lenSeq = int(next(gen))
        seq = next(gen)
        result = process_case(prep_comb(comb), prep_opp(opp), seq)
        yield 'Case #{0}: {1}\n'.format(ci, '[' + ', '.join(result) + ']')
    
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

##start('B-test')
##start('B-small-attempt0')
start('B-large')
