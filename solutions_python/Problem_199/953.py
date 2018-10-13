#!/bin/python
import sys
input_filename, = sys.argv[1:]
input = open(input_filename)
assert input_filename.endswith('.in'), input_filename
output = open(input_filename[:-3]+'.out', 'w')
    
T = int(input.readline())

def flip_all(s):
    return ''.join([{'+': '-', '-': '+'}[c] for c in s])

assert flip_all("++-") == "--+"

def flip(s, i, K):
    return s[:i] + flip_all(s[i:i+K]) + s[i+K:]

assert flip("++-", 1, 2) == "+-+"

def run(s, K):
    n = len(s)
    count = 0

    for i in range(n-K+1):
        if s[i] == '-':
            s = flip(s, i, K)
            count += 1

    for c in s:
        if c != '+':
            return 'IMPOSSIBLE'

    return count
            
            
def solve():
    s, K = input.readline().split(' ')
    K = int(K)
    return run(s, K)

for t in range(T):
    print >> output, 'Case #{}: {}'.format(t+1,solve())

