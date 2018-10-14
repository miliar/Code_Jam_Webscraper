import sys
import math

def solve(xi, vi, K, B, T):
    good = []
    for i in range(len(xi)):
        pos = xi[i] + vi[i] * T
        if pos>=B:
            good.append(i)
    if len(good)<K:
        return 'IMPOSSIBLE'
    good = list(good[-K:])
    res = 0
    for i in range(len(good)):
        res += len(xi)-1 - good[i] - i
    return res

def do_test(input):
    line = input.readline().strip(' \r\n\t').split()
    N,K,B,T = (int(line[i]) for i in range(4))
    line = input.readline().strip(' \r\n\t').split()
    xi = [int(line[i]) for i in range(N)]
    line = input.readline().strip(' \r\n\t').split()
    vi = [int(line[i]) for i in range(N)]
    
    res = solve(xi, vi, K, B, T)
    return str(res)

input = sys.stdin

N = int(input.readline())

for test in range(N):
    answer = do_test(input)
    print 'Case #%d: %s' % (test+1, answer)
    sys.stdout.flush()
    
