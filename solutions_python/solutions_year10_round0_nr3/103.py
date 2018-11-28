import string
import itertools
import collections
import sys
import pdb

def process_case(R,k,groups):
    if sum(groups) <= k:
        return R * sum(groups)
    ravenue = 0
    n = len(groups)
    idx = 0
    runs = R
    run_tab = [0 for i in range(n)]
    ravenue_tab = [0 for i in range(n)]
    while runs > 0:
        cnt=0
        while (cnt+groups[idx] <= k):
            cnt += groups[idx]
            idx = (idx+1) % n
        ravenue += cnt
        runs -= 1
        
        if run_tab[idx] > 0:
            dr = run_tab[idx] - runs
            drav = ravenue - ravenue_tab[idx]
            mul = runs // dr
            if (mul > 0):
                runs -= mul * dr
                ravenue += mul * drav
        run_tab[idx] = runs
        ravenue_tab[idx] = ravenue
    return ravenue

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        R,k,N = line_of_numbers(next(lines))[:3]
        groups = line_of_numbers(next(lines))
        result = process_case(R,k,groups)
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

start('C-test')
