# python 3
import string
import itertools
import sys

def process_case(stands, d):
    n = len(stands)
    stands.sort()
    cnt_sum = [0]
    cnt_sum.extend([stands[i][1] for i in range(n)])
    for i in range(1,n+1):
        cnt_sum[i] += cnt_sum[i-1]
#    print(stands)
#    print(cnt_sum)
    result = 0
    for i in range(n):
        for j in range(i+1):
            cnt = cnt_sum[i+1] - cnt_sum[j]
            if cnt==1:
                continue
            ini_spread = stands[i][0] - stands[j][0]
            spread = (cnt-1) * d
##            print('{0} {1}:   {2} -> {3}'.format(j, i, ini_spread, spread))
            result = max(result, (spread - ini_spread) / 2)
    return result

def result_gen(lines):
    ncases = int(next(lines))
    for ci in range(1,ncases+1):
        c,d = line_of_numbers(next(lines))
        stands = [line_of_numbers(next(lines)) for i in range(c)]
        result = process_case(stands, d)
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
##start('B-small-attempt0')
start('B-large')
