#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Uses https://github.com/rkistner/contest-algorithms

import sys


def debug(*args):
    print(*args, file=sys.stderr)

def same(a, b):
    return a == b
    if a == 0 and b == 0:
        return True
    return abs(a-b)/(abs(a)+abs(b)) < 0.0000001

fin = sys.stdin
T = int(fin.readline())
for case in range(1, T + 1):
    head = fin.readline().split()
    N = int(head[0])
    V = float(head[1])
    X = float(head[2])

    flows = []
    for i in range(N):
        r, c = map(float, fin.readline().split())
        r /= V
        c /= X
        flows.append((r, c))


    result = None
    if N == 1:
        if same(flows[0][1], 1):
            result = 1/flows[0][0]
        else:
            debug(case, 'IMPOSSIBLE - n=1 and invalid flow', flows)
            result = None
    elif N == 2:
        x1 = flows[0][1]
        x2 = flows[1][1]
        r1 = flows[0][0]
        r2 = flows[1][0]

        if same(x1, x2):
            if same(x1, 1) or same(x2, 1):
                r = r1 + r2
                result = 1/r
            else:
                debug(case, 'IMPOSSIBLE')
                result = None
        else:
            v1 = (1-x2)/(x1-x2)
            t1 = v1/r1
            v2 = 1-v1
            t2 = v2/r2
            if (v1 < 0 and not same(v1, 0)) or (v2 < 0 and not same(v2, 0)):
                debug(case, 'IMPOSSIBLE - need negative flow', flows)
                result = None
            else:
                result = max(t1, t2)


        if result is not None:
            if x1 > 1 and x2 > 1:
                raise Exception("FOO")
            if x1 < 1 and x2 < 1:
                raise Exception("BAR")

    else:
        debug(case, 'Too large N', flows)


    if result is None:
        print("Case #%d: IMPOSSIBLE" % (case))
    else:
        print("Case #%d: %.10f" % (case, result))

"""
5 IMPOSSIBLE - n=1 and invalid flow [(0.5065784290553849, 0.9999930078853573)]
7 IMPOSSIBLE - need negative flow [(7.000007000007e-06, 3.2941648461705153), (2.0000020000020002e-06, 1.0000644250648643)]
20 IMPOSSIBLE
45 IMPOSSIBLE - need negative flow [(0.8844685997744044, 0.3729357156665556), (0.4674556594959117, 0.1578028405375057)]
58 IMPOSSIBLE - need negative flow [(0.09639824257412465, 2.2674094006991425), (1.708984008282862, 4.549410255765411)]
65 IMPOSSIBLE - need negative flow [(1.0, 1.001), (1.0, 1.002)]
67 IMPOSSIBLE - n=1 and invalid flow [(0.31994045973707197, 222.829)]
71 IMPOSSIBLE - need negative flow [(2.0, 0.9999958534441293), (499999.49999999994, 0.15433066295135262)]
77 IMPOSSIBLE - need negative flow [(1.836245658197279, 1.396698781593187), (1.5251835676387264, 1.4236068137716646)]
80 IMPOSSIBLE - need negative flow [(6.0, 0.9999989989989989), (4.0, 0.9979979979979979)]
81 IMPOSSIBLE - need negative flow [(0.345442002741243, 0.9999884315662069), (3.9922528115894673, 0.2476295556130764)]
83 IMPOSSIBLE - n=1 and invalid flow [(0.6161911348919223, 1.379364032840781)]
94 IMPOSSIBLE - n=1 and invalid flow [(0.40686398047122074, 0.5395495495495496)]
96 IMPOSSIBLE - need negative flow [(1.6347387167917022, 1.1186229467704087), (6.7309747252443035, 1.0000135852784984)]
"""