from itertools import *

def solve(N, nines):
    if ''.join (sorted (N)) == N:
        return N, nines
    return solve (str(int(N[:-1])-1), nines + 1)

for case in range(int(raw_input())):
    N, = map(int,raw_input().split())
    ansN, ans9 = solve(str (N), 0)
    ans = int(ansN + '9' * ans9)
    print "Case #%d: %d" % (case+1, ans)
