import string
import itertools
import sys

def process_case(p,M,prices):
##    print(p)
##    print(M)
##    print(prices)
    N = 1<<p
    result = 0
    for lev in range(p):
        group_size = 2<<lev
        matches = N // group_size
        for mi in range(matches):
            buy = False
            for gi in range(group_size):
                ti = mi * group_size + gi
##                print('{0}: M[{1}] = {2}'.format(lev, ti, M[ti]));
                if (M[ti] <= lev):
                    buy = True
##                    print('*')
            if (buy):
##                print('buy for l {0} group {1}'.format(lev, gi))
                result += 1
    return result

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        p = int(next(lines))
        M = line_of_numbers(next(lines))[:1<<p]
        prices = []
        for lev in range(p):
            vals = line_of_numbers(next(lines))[:1<<(p-lev-1)]
            prices.append(vals)
        result = process_case(p,M,prices)
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

##start('B-test')
start('B-small-attempt1')
