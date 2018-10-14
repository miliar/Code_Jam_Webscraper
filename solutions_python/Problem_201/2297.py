#!/usr/bin/env python2

import sys
stdin = sys.stdin.readlines()
cases = int(stdin.pop(0))
for case in xrange(cases):
    n, k = stdin.pop(0).strip().split()
    n = int(n)
    k = int(k)
    init_stalls = [True] + [False] * n + [True]
    stalls = []
    for i in xrange(n+2):
        if init_stalls[i]:
            stalls.append((init_stalls[i], 0, 0, i))
        else:
            stalls.append((init_stalls[i], i-1, n-i, i))
    runs = [[n, 1]]
    i = 0
    while i < k:
        maxrun, j = runs.pop(0)
        i += j
        if maxrun == 1:
            maxlr = minlr = 0
        elif maxrun%2:
            maxlr = minlr = (maxrun-1)/2
        else:
            maxlr = maxrun/2
            minlr = maxrun/2 - 1
        if maxlr:
            appended = False
            for a in xrange(len(runs)):
                if runs[a][0] == maxlr:
                    runs[a][1] += j
                    appended = True
                    break
            if not appended:
                runs.append([maxlr, j])
        if minlr:
            appended = False
            for a in xrange(len(runs)):
                if runs[a][0] == minlr:
                    runs[a][1] += j
                    appended = True
                    break
            if not appended:
                runs.append([minlr, j])
        # minlrstall = emptystalls[0]
        # minlr = min(minlrstall[1], minlrstall[2])
        # maxlr = max(minlrstall[1], minlrstall[2])
        # minstall = emptystalls[0]
        # ind = 0
        # i = 1
        # for stall in emptystalls[1:]:
        #     stallmin = min(stall[1], stall[2])
        #     if stallmin > minlr:
        #         minstall = stall
        #         ind = i
        #         minlr = stallmin
        #         maxlr = max(stall[1], stall[2])
        #     elif stallmin == minlr:
        #         stallmax = max(stall[1], stall[2])
        #         if stallmax > maxlr:
        #             minstall = stall
        #             maxlr = stallmax
        #             ind = i
        #     i += 1
        # i = ind - 1
        # j = minstall[3] - 1
        # r = 0
        # while i > -1 and emptystalls[i][3] == j:
        #     emptystalls[i] = (emptystalls[i][0], emptystalls[i][1], r, emptystalls[i][3])
        #     r += 1
        #     j -= 1
        #     i -= 1
        # i = ind + 1
        # j = minstall[3] + 1
        # l = 0
        # lenes = len(emptystalls)
        # while i < lenes and emptystalls[i][3] == j:
        #     emptystalls[i] = (emptystalls[i][0], l, emptystalls[i][2], emptystalls[i][3])
        #     l += 1
        #     j += 1
        #     i += 1
        # emptystalls = emptystalls[:ind] + emptystalls[ind+1:]
    print "Case #"+str(case+1)+": "+str(maxlr)+" "+str(minlr)
