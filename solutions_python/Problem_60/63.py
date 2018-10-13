#!/usr/bin/python

SIZE = 'large'
PROBLEM = 'B'
DATASET = PROBLEM + '-' + SIZE
IFILE = DATASET + '.in'
OFILE = DATASET + '.out'

def can_doit(B, T, pos, spd):
    lngth = B - pos
    max_lngth = T*spd
    return lngth <= max_lngth

def solve(N, K, B, T, poss, spds):
    if K == 0: return 0
    penalty = 0
    swaps = 0
    for i in xrange(N-1, -1, -1):
        if can_doit(B, T, poss[i], spds[i]):
            swaps += penalty
            K -= 1
            if K == 0: return swaps
        else:
            penalty += 1
    return 'IMPOSSIBLE'

ifile = open(IFILE, 'r')
ofile = open(OFILE, 'w')
C = int(ifile.readline())
for i in xrange(C):
    line = (int(a) for a in ifile.readline().strip().split(' '))
    N, K, B, T = line
    poss = [int(a) for a in ifile.readline().strip().split(' ')]
    assert len(poss) == N
    spds = [int(a) for a in ifile.readline().strip().split(' ')]
    assert len(spds) == N
    ofile.write('Case #%s: %s\n' % (i+1,str(solve(N, K, B, T, poss, spds))))
ifile.close()
ofile.close()
