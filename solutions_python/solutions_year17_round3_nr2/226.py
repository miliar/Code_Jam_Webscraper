#NTheo
#SMALL ONLY
from __future__ import division

T = int(raw_input())
for t in range(T):
    Ac, Aj = [int(x) for x in raw_input().split()]
    if Ac == 1 or Aj == 1:
        [raw_input() for x in range(Ac + Aj)]
        print('Case #{}: {}'.format(t+1, 2))
    else:
        i1 = [int(x) for x in raw_input().split()]
        i2 = [int(x) for x in raw_input().split()]
        if i2[0] < i1[0]:
            i2, i1 = i1, i2
        w = 2 if min(i2[1] - i1[0], i1[1] + 1440 - i2[0]) <= 720 else 4
        print('Case #{}: {}'.format(t+1, w)) 
        