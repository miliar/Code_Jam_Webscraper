#!/usr/bin/python

import math

# k will be <= P
def solve(N, P, R, Q):
    #print N, P, R, Q
    kit_matrix = []
    possible_ks = set()
    for i in range(N):
        Q[i].sort()
        kit_row = []
        for q in Q[i]:
            low = int(math.ceil(float(q) / R[i] / 1.1))
            high = int(math.floor(float(q) / R[i] / 0.9))
            k = set(range(low, high + 1))
            if len(k) > 0:
                kit_row.append(k)
                possible_ks.update(k)
        kit_matrix.append(kit_row)
    
    possible_ks = sorted(list(possible_ks))
    j = 0
    num_kits = 0
    #print possible_ks
    while j < len(possible_ks):
        #print kit_matrix
        k = possible_ks[j]
        #print k
        possible = True
        for i in range(N):
            while len(kit_matrix[i]) > 0 and max(kit_matrix[i][0]) < k:
                kit_matrix[i].pop(0)
            if len(kit_matrix[i]) == 0:
                return num_kits
            #print i, kit_matrix[i][0]
            if k not in kit_matrix[i][0]:
                possible = False
                break
        #print possible
        if possible:
            num_kits += 1
            for i in range(N):
                kit_matrix[i].pop(0)
        else:
            j += 1
    return num_kits

T = int(raw_input())
for t in range(T):
    N, P = map(int, raw_input().split())
    R = map(int, raw_input().split())
    Q = []
    for r in range(N):
        Q.append(map(int, raw_input().split()))
        
    k = solve(N, P, R, Q)
    print "Case #%d: %d" % (t + 1, k)