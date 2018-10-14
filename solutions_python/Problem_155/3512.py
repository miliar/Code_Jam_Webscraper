FILENAME = "A-small-attempt0"
LOCAL = 0

import sys
if LOCAL == 1:
    sys.stdin = open(FILENAME + ".in", 'r')
    sys.stdout = open(FILENAME + ".out", 'w')

def get_line(): return input()
def get_int(): return int(get_line())


def solve():
    N, S = get_line().split()
    N = int(N)
    S = [int(_) for _ in S]
    accum = 0
    invite = 0
    for i in range(1, N+1):
        accum += S[i-1]
        if i > accum:
            invite += i - accum
            accum += i - accum
    return invite

for case in range(get_int()):
    print('Case #%d: %s' % (case+1, solve()))