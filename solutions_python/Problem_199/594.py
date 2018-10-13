import sys
import itertools

import numpy as np

def parse(line):
    S,K = line.split()
    return np.array([('-','+').index(c) for c in S]), int(K)

def solve(case):
    S,K = case
    y = 0
    for i in range(len(S)-K+1):
        if S[i] == 0:
            S[i:i+K] = (S[i:i+K] + 1) % 2
            y += 1
    if S[-K+1:].all():
        return y
    else:
        return 'IMPOSSIBLE'

input_file = sys.argv[1]
with open(input_file) as f:
    lines = [line.strip() for line in f]
cases = map(parse,lines[1:])
output = map(solve,cases)
output_file = input_file.replace('input','output')
with open(output_file,'w') as f:
    for i,y in enumerate(output):
        f.write(f'Case #{i+1}: {y}\n')
