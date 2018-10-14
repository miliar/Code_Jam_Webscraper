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

i = 1
while i <= n:
    (N, K, B, T) = map(int, input_file.readline().split(" "))
    
    pos = map(int, input_file.readline().split(" "))
    vels = map(int, input_file.readline().split(" "))
    fast = [True]*N
    
    for chick in range(N-1, -1, -1):
        if vels[chick] * T < B - pos[chick]:
            fast[chick] = False
    if sum(fast) < K:
        res = "IMPOSSIBLE"
    else:
        res = 0
        for chick in range(N-1, -1, -1):
            if not fast[chick]:
                continue
            for obstacle in range(N-1, chick, -1):
                if not fast[obstacle]:
                    res += 1
            K -= 1
            if K == 0:
                break
    
    res = 'Case #' + str(i) + ': ' + str(res)
    print(res)
    if output_file is not None:
        output_file.write(res + '\n')
    i += 1

input_file.close()
if output_file is not None:
    output_file.close()
