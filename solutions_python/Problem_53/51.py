import sys
import math

def solve(N, K):
    period = 2**N
    return K % period == period - 1

def do_test(input):
    line = input.readline().strip(' \r\n\t').split()
    N = int(line[0])
    K = int(line[1])
    res = solve(N, K)
    return 'ON' if res else 'OFF'

input = sys.stdin

N = int(input.readline())

for test in range(N):
    answer = do_test(input)
    print 'Case #%d: %s' % (test+1, answer)
    sys.stdout.flush()
    
