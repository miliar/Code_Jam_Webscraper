#!/usr/bin/python

import heapq

def max_min_distance(N, K):
    tol = 1
    level_tol = 1 # 2^ (level - 1)
    l = []
    l.append([1,N,1,N,0])
    
    while tol < K:
        level = l[-1][0]
        mind = (l[-1][3] - 1) / 2
        maxd = l[-1][1] - 1 - (l[-1][1] - 1) / 2
        tmp = [level + 1, maxd, l[-1][2], mind, l[-1][-1]]
        if (mind == (l[-1][1] - 1) / 2):
            tmp[-1] += l[-1][2]
        else:
            tmp[2] += l[-1][2]
        if (maxd == l[-1][3] - 1 - (l[-1][3] - 1) / 2):
            tmp[2] += l[-1][-1]
        else:
            tmp[-1] += l[-1][-1]
        
        l.append(tmp)
        level_tol = level_tol * 2
        tol += level_tol
        
    dif = K - (tol - level_tol)
    if l[-1][2] < dif:
        seg = l[-1][3]
    else:
        seg = l[-1][1]
    return seg - 1 - (seg - 1) / 2, (seg - 1) / 2
    
        
        
    

if __name__ == "__main__":
    t = int(raw_input())
    for i in range(0, t):
        s = raw_input().split()
        N = int(s[0])
        K = int(s[1])
        maxd, mind = max_min_distance(N, K)
        print "Case #" + str(i + 1) + ":", maxd, mind
        
        
