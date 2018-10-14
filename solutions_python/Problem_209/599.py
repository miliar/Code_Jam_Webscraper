#!/bin/python
import math

T = int(raw_input().strip())


def getSurface(p):
    return math.pi * (p[0] * p[0] + 2 * p[0] * p[1])


def getHeight(p):
    return math.pi * 2 * p[0] * p[1]


# def getSurface(selected):
#

for c in range(1, T + 1):
    N, K = map(int, raw_input().split())
    ps = [map(int, raw_input().split()) for _ in range(N)]
    ps = sorted([(p[0], p[1], getSurface(p), getHeight(p), i) for (i, p) in enumerate(ps)], reverse=True)
    hps = sorted(ps, key=lambda x: x[3])

    surface = ps[0][2]
    for i in range(1, len(ps)):
        surface += ps[i][3]
    # print ps

    for o in range(N - K):
        # print o, surface
        c1 = surface - ps[0][2] + ps[1][2] - ps[1][3]
        j = 0
        while hps[j][-1] == ps[0][-1]:
            j += 1
        c2 = surface - hps[j][3]

        # print c1, c2, ps[0], hps[j]
        if c1 > c2:
            k = 0
            while ps[0][-1] != hps[k][-1]:
                k += 1
            # print 'remove 1', ps[0], hps[k]
            del hps[k]
            del ps[0]
            surface = c1

        else:
            k = 0
            while hps[j][-1] != ps[k][-1]:
                k += 1
            # print 'remove 2', ps[k], hps[j]
            del hps[j]
            del ps[k]
            surface = c2


    # print ps
    #
    #
    # selected=[]
    # # surface = ps[0][0];
    # selected.append(ps[0])
    # ps[0] = None
    #
    # if(len(selected) < K):
    #     selected += ps[1:K]
    #
    # selected.sort(key=lambda x:x[1], reverse=True)
    # surface = selected[0][0]
    # for i in range(1, len(selected)):
    #     surface += selected[i][3]

    # for i in range(1, len(ps)):
    #     print i
    #     if len(selected) == K: break
    #     if ps[i][1] <= selected[-1][1]:
    #         selected.append(ps[i])
    #         surface += ps[i][3]
    #         ps[i] = None

    # if len(selected) < K: #need to grab few big ones


    # print selected, surface


    # print N, K, ps, [(getSurface(p), getHeight(p)) for p in ps]

    # print D, N, horses
    # times = [(D-k)*1./s for k,s in horses]


    # ans = D*1./max(times)
    print 'Case #%d: %.10f' % (c, surface)
