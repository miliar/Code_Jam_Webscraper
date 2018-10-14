from decimal import Decimal
from sys import stdin

input_it = iter(stdin)

T = int(input_it.next())

for t in range(T):

    # interpret input
    N = int(input_it.next())
    WN = sorted(Decimal(c) for c in input_it.next().split())
    WK = sorted(Decimal(c) for c in input_it.next().split())

    # first calculate Naomi's top score in deceitful war
    y = 0
    wk_i = 0

    for wn in WN:
        if wn < WK[wk_i]:
            continue
        else:
            y += 1
            wk_i += 1

    # then calculate Naomi's top score in war
    z = 0
    wn_i = 0

    for wk in WK:
        if wk < WN[wn_i]:
            continue
        else:
            z += 1
            wn_i += 1

    z = N - z

    print 'Case #{t}: {y} {z}'.format(t=t+1, y=y, z=z)
