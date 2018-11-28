import sys

lines = (line[:-1] for line in sys.stdin)
T = int(next(lines))

for Ti in range(1, T + 1):
    Smax, S = next(lines).split(' ')
    Smax = int(Smax)

    up = 0
    friends = 0
    for Si, Sk in enumerate(S):
        miss = max(0, Si - up)
        friends += miss
        up += int(Sk) + miss

    print('Case #{}: {}'.format(Ti, friends))
