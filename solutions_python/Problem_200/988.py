#!/bin/python
import sys
input_filename, = sys.argv[1:]
input = open(input_filename)
assert input_filename.endswith('.in'), input_filename
output = open(input_filename[:-3]+'.out', 'w')

def is_tidy(s):
    last = '0'
    for c in s:
        if c<last:
            return False
        last = c
    return True

assert is_tidy("123345")
assert not is_tidy("1232345")

def solve(N):
    if is_tidy(str(N)):
        return N
    return solve(N/10-1)*10 + 9
        
def run():
    N = int(input.readline())
    return solve(N)

T = int(input.readline())
for t in range(T):
    print >> output, 'Case #{}: {}'.format(t+1,run())
