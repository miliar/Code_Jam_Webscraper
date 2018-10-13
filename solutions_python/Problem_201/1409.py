#!/usr/bin/env python
import sys

try:
    xrange
except NameError:
    xrange = range

def solve(N, K):
    Intervals = {
        int(N): 1
    }
    Min = 0
    Max = 0
    Choosed = 0
    while Choosed < K:
        MaxN = sorted(Intervals.keys())[-1]
        assert(MaxN > 0)
        if MaxN % 2 == 0:
            Min = (MaxN - 1)//2
            Max = Min + 1        
        else:
            Min = MaxN//2
            Max = Min
        assert(Intervals[MaxN] > 0)
        ToChoose = min(K - Choosed, Intervals[MaxN])
        if Intervals[MaxN] == ToChoose:
            del Intervals[MaxN]
        else:
            Intervals[MaxN] -= ToChoose
        Choosed += ToChoose
        Intervals[Max] = Intervals.get(Max, 0) + ToChoose
        Intervals[Min] = Intervals.get(Min, 0) + ToChoose
    return Max, Min

lines = [l.strip() for l in sys.stdin.readlines()]
T = int(lines[0])
assert(T == len(lines)-1)

for i in range(1, T+1):
    strN, strK = lines[i].strip().split()
    N = int(strN)
    K = int(strK)
    Max, Min = solve(N, K)
    sys.stdout.write("Case #{}: {} {}\n".format(i, Max, Min))
