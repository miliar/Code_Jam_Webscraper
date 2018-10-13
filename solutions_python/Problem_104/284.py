from itertools import combinations
import sys

inp = sys.stdin

T = int(inp.readline())
for case_number in range(1, T + 1):
    S = map(int, inp.readline().split())
    N = S.pop(0)
    assert N == len(S)
    sets = {}
    print 'Case #%d:' % case_number
    for l in range(1, N + 1):
        for ss in combinations(S, l):
            s = sum(ss)
            sss = sorted(ss)
            if s in sets and sets[s] != sss:
                print ' '.join(map(str, sss))
                print ' '.join(map(str, sets[s]))
                break
            sets[s] = sss
        else:
            continue
        break
    else:
        print 'Impossible'

