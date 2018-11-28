#!/usr/env/bin/python
from sys import argv
from itertools import combinations

if len(argv) < 2:
    print("Insufficient arguments. Usage: python script.py <input file> [<output file>]")
    exit()

input_file = open(argv[1])

output_file = None
if len(argv) >= 3:
    output_file = open(argv[2], 'w')

n = int(input_file.readline())

memoized = dict()

i = 1
while i <= n:
    N = int(input_file.readline())
    
    if N in memoized:
        res = memoized[N]
    else:
        res = 0
        nums = tuple(range(2, N))
        for j in nums+(N,):
            for comb in combinations(nums, j-2):
                comb += (N,)
                num = comb[0]
                try:
                    while num < N:
                        num = comb[num-1]
                    if num == N:
                        res += 1
                except IndexError:
                    pass
        memoized[N] = res
    
    res = 'Case #' + str(i) + ': ' + str(res%100003)
    print(res)
    if output_file is not None:
        output_file.write(res + '\n')
    i += 1

input_file.close()
if output_file is not None:
    output_file.close()
