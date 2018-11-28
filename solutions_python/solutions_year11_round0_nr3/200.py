import sys
import math

def solve(vals):
    xorsum = 0
    for v in vals:
        xorsum ^= v
    if xorsum!=0:    
        return 'NO'
    return sum(vals) - min(vals)

def do_test(input):
    line = input.readline().strip(' \r\n\t').split()
    M = int(line[0])
    line = input.readline().strip(' \r\n\t').split()
    assert len(line)==M
    vals = [int(s) for s in line]
    res = solve(vals)
    return str(res)

input = sys.stdin

N = int(input.readline())

for test in range(N):
    answer = do_test(input)
    print 'Case #%d: %s' % (test+1, answer)
    sys.stdout.flush()
    
