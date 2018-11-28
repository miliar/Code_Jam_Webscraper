# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 18:30:17 2017

@author: Emad Yehya
"""


fi = file('C-large.in', 'r')
fo = file('out.txt', 'w')

T = int(fi.readline()[:-1])



def get_nbs(s):
    if(s % 2 == 1):
        return ((s-1)/2, (s-1)/2)
    else:
        return ((s)/2, (s)/2 - 1)

def stupid_solve(N, K):
    L = [N]
    for i in range(1, K):
        L.sort()
        L.reverse()
        ANS = get_nbs(L[i-1])
        L.append(ANS[0])
        L.append(ANS[1])
    return get_nbs(L[K-1])


def solve_for_NK(N, K):
    vals = (N, N-1)
    dist = (1, 0)
    while(True):
#        print K, vals, dist
        K -= dist[0]
        if(K <= 0):
            return get_nbs(vals[0])
        K -= dist[1]
        if(K <= 0):
            return get_nbs(vals[1])

        if(vals[0] % 2 != 0):
            #first one is odd
            vals = ((vals[0]-1)/2, (vals[0]-1)/2 - 1)
            dist = (2*dist[0] + dist[1], dist[1])
        else:
            #second is odd
            vals = ((vals[0]-1)/2 + 1, (vals[0]-1)/2)
            dist = (dist[0], dist[0] + 2*dist[1])

    
for t in range(1, T+1):
    line = fi.readline()[:-1]
    N = int(line.split(' ')[0])
    K = int(line.split(' ')[1])
#    #find first break, if any
    ANS = solve_for_NK(N, K)
#    print "Case #" + str(t) + ": "+ str(ANS[0])+ " " + str(ANS[1])
#    fo.write(str(N) + " " + str(K) + "\n")
    fo.write("Case #" + str(t) + ": "+ str(ANS[0])+ " " + str(ANS[1]) + "\n")
#    ANS = stupid_solve(N, K)
#    fo.write("Case #" + str(t) + ": "+ str(ANS[0])+ " " + str(ANS[1]) + "\n")
    
    
fi.close()
fo.close()