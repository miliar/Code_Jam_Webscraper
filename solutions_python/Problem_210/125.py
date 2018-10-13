# Google codejam 2017B
# A. 

import math

for t in range(1, int(input()) + 1):
    ac, aj = map(int, input().split())
    cs = []
    for _ in range(ac):
        c, d = map(int, input().split())
        cs.append((c, d))
    js = []
    for _ in range(aj):
        j, k = map(int, input().split())
        js.append((j, k))

    result = 2
    if ac == 2:
        if cs[0][0] < cs[1][1]:
            if cs[1][1] - cs[0][0] > 720 and cs[1][0] - cs[0][1] < 720:
                result = 4
        else:
            if cs[0][1] - cs[1][0] > 720 and cs[0][0] - cs[1][1] < 720:
                result = 4
    elif aj == 2:
        if js[0][0] < js[1][1]:
            if js[1][1] - js[0][0] > 720 and js[1][0] - js[0][1] < 720:
                result = 4
        else:
            if js[0][1] - js[1][0] > 720 and js[0][0] - js[1][1] < 720:
                result = 4

    print ("Case #{}: {}".format(t, result))
