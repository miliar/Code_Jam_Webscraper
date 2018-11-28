# This code was interpreted using CPython 3.3.4
# python3 Main.py < data.in > data.out

import bisect
import copy


def war(in1, in2):
    player_1 = copy.deepcopy(in1)
    player_2 = copy.deepcopy(in2)

    for w in player_1:
        pos = bisect.bisect(player_2, w)
        if pos == len(player_2):
            break

        player_2.remove(player_2[pos])

    return len(player_2)

T = int(input())
for T_ in range(1, T+1):
    N = int(input())

    naomi = [float(x) for x in input().split(' ')]
    ken = [float(x) for x in input().split(' ')]

    naomi.sort(), ken.sort()

    A1 = len(naomi) - war(ken, naomi)
    A2 = war(naomi, ken)

    print("Case #{0}: {1} {2}".format(T_, A1, A2))