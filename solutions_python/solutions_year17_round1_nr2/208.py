#!/usr/bin/env python

from ortools.graph import pywrapgraph


margin = 1e-6

for nnn in xrange(1, int(raw_input())+1):
    print "Case #%d:" % (nnn),
    N, P = [int(x) for x in raw_input().split()]
    R = [int(x) for x in raw_input().split()]
    Q = [[int(x) for x in raw_input().split()] for _ in xrange(N)]

    max_flow = pywrapgraph.SimpleMaxFlow()
    START, END = N*P, N*P+1
    servings = [[0]*P for _ in xrange(N)]
    for i in xrange(N):
        for j in xrange(P):
            lo, hi = int(0.909*Q[i][j]/R[i]), int(1.112*Q[i][j]/R[i])
            possible = []
            for num_servings in xrange(lo, hi+1):
                if num_servings*R[i]*0.9 - margin < Q[i][j] < num_servings*R[i]*1.1 + margin:
                    possible.append(num_servings)
            servings[i][j] = set(possible)
            if len(servings[i][j]) > 0:
                if i == 0:
                    max_flow.AddArcWithCapacity(START, j, 1)
                elif i > 0:
                    for k in xrange(P):
                        if len(servings[i][j] & servings[i-1][k]) > 0:
                            max_flow.AddArcWithCapacity((i-1)*P+k, i*P+j, 1)
                if i == N-1:
                    max_flow.AddArcWithCapacity((N-1)*P+j, END, 1)
    max_flow.Solve(START, END)
    print max_flow.OptimalFlow()

