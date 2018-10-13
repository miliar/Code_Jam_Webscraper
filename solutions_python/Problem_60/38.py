#!/usr/bin/env python

import sys
import copy
input = sys.stdin

def getFinishTimes(N, X, V, swaps):
    times = []
    for i in range(N):
        time = X[i] / V[i]
        if X[i] % V[i]:
            time += 1
        for free_time, j in swaps[i]:
            if times[j] > time:
                time = times[j]
        times.append(time)
    return times

def main():
    T = int(input.readline())
    for t in range(1, T + 1):
        N, K, B, T = map(int, input.readline().split())
        X = map(int, input.readline().split())
        X = [B - val for val in X][::-1]
        V = map(int, input.readline().split())
        V = V[::-1]

        if K == 0:
            print "Case #%s: %s" % (t, 0)
            continue

        swaps = [[] for i in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                if V[j] > V[i]:
                    free_time = (X[j] - X[i] - 1) / (V[j] - V[i])
                    if free_time >= X[i] / V[i]:
                        continue
                    swaps[j].append((free_time, i))
        for i in range(N):
#            print i, swaps[i]
            swaps[i].sort()

#        print X
#        print V
        done = False
        cnt = 0
        while not done:
            times = getFinishTimes(N, X, V, swaps)
#            print times
#            print sorted(times)
            if sorted(times)[K - 1] <= T:
                done = True
            else:
                bst = 0x3f3f3f3f
                bstNod = -1

                for i in range(N):
                    if len(swaps[i]) == 0:
                        continue
                    if times[i] <= T:
                        continue
                    min_time = X[i] / V[i]
                    if X[i] % V[i]:
                        min_time += 1
                    if min_time > T:
                        continue

                    aux = copy.copy(swaps[i])
                    curDone = False
                    while not curDone:
                        toRemove = max((times[nod], (time, nod)) for (time, nod) in swaps[i])
                        swaps[i].remove(toRemove[1])
                        curTimes = getFinishTimes(N, X, V, swaps)
                        if curTimes[i] <= T:
                            curDone = True
#                    print "\t\t", i, swaps[i], len(aux) - len(swaps[i]), "-", curTimes[i], T
                    if len(aux) - len(swaps[i]) < bst:
                        bst = len(aux) - len(swaps[i])
                        bstNod = i
                    swaps[i] = aux
#                    print "\t\t", i, len(aux), "-", curTimes[i], T
#
#                print "\t", bst
#                print "\t", bstNod
                if bst == 0x3f3f3f3f:
                    done = True
                    cnt = "IMPOSSIBLE"
                else:
                    i = bstNod
                    curDone = False
                    while not curDone:
                        toRemove = max((times[nod], (time, nod)) for (time, nod) in swaps[i])
                        swaps[i].remove(toRemove[1])
                        curTimes = getFinishTimes(N, X, V, swaps)
                        if curTimes[i] <= T:
                            curDone = True
                        cnt += 1

        print "Case #%s: %s" % (t, cnt)
    return 0

if __name__ == "__main__":
    main()

