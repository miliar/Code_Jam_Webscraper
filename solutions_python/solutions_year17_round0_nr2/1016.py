from __future__ import print_function
import sys
import itertools

def solve():
    # parse input
    N = map(int, list(raw_input()))

    print(N, file=sys.stderr)
    # solve
    first_digit = N[0]
    first_less = None
    for i in range(1, len(N)):
        if N[i] < N[i-1]:
            first_less = i
            break
    print(first_less, file=sys.stderr)
    if first_less is None:
        return ''.join(map(str, N))
    for i in range(first_less-1, -1, -1):
        if N[i] != N[first_less - 1]:
            break
    else:
        if N[0] == 1:
            return '9'*(len(N)-1)
        else:
            return str(N[0]-1) + '9'*(len(N)-1)

    return ''.join(map(str, N[:i+1])) + str(N[first_less-1] - 1)*(first_less - i - 1) + '9'*(len(N) - first_less)

T = int(raw_input())
for case in xrange(T):
    print(case, file=sys.stderr)
    print("Case #%d: %s"%(case+1, solve()))
