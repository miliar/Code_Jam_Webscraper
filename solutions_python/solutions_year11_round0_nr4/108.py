# -*- coding: utf-8 -*-

import sys

import math

input_file=open(sys.argv[1]) if len(sys.argv)>1 else sys.stdin
output_file=open(sys.argv[2], 'w') if len(sys.argv)>2 else sys.stdout


'''
facts=[math.factorial(i) for i in range(1001)]

def all_wrong(n):
    return sum((-1 if i&1 else 1) * facts[n]//facts[i] for i in range(n+1))

wrongs=[all_wrong(i) for i in range(100)]

def C(n, k):
    return facts[n]//facts[k]//facts[n-k]
'''

def parse(line):
    return list(map(lambda x:int(x)-1, line.split()))

def find_all_rings(array):
    A = array[:]
    Z = sorted(array)

    rings=[]
    for i in range(len(A)):
        if A[i] is not None:
            next_i = A[i]
            A[i] = None
            ring = {next_i}
            while (next_i is not None) and (next_i != Z[i]):
                A[next_i], next_i = None, A[next_i]
                ring.add(next_i)
            else:
                rings.append(ring)

    return rings

def solve(line):
    array=parse(line)

    all_length = map(len, find_all_rings(array))

    return sum(filter(lambda x:x>1, all_length))


if __name__=='__main__':
    cases = int(next(input_file))

    for case in range(1, cases+1):
        next(input_file)

        print('Case #{}: {:.6f}'.format(case, solve(next(input_file))),
              file=output_file)
