'''
Created on 2012/04/14

@author: teraotsuyoshi
'''

from itertools import *

def max_point(total, surp):
    m = 0
    
    if total == 0:
        return 0
    elif total == 1:
        return 1
    elif total == 2:
        if surp:
            return 2
        else:
            return 1
    elif total >= 28:
        return 10

    if surp:
        if total % 3 == 0:
            m = total / 3 + 1
        elif total % 3 == 1:
            m = total / 3 + 1
        else:
            m = total / 3 + 2
    else:
        m = total / 3
        if m * 3 < total:
            m = m + 1
    
    return m

def make_surp_table(N, S):
    surp_table = [(x < S) for x in range(N)]
    used = []
    for x in permutations(surp_table):
        if x in used:
            continue
        used.append(x)    
        
    return used


if __name__ == '__main__':
    lines = open("B-small-attempt0.in").readlines()
    T = int(lines[0])
    for i in range(1, T+1):
        (N,S,P) = lines[i].split()[:3]
        N = int(N)
        S = int(S)
        P = int(P)
        t = []
        for x in lines[i].split()[3:]:
            t.append(int(x))

        surp_table = make_surp_table(N, S)
        mm = 0
        for surp in surp_table:
            m = 0
            for x in imap(max_point,t, surp):
                if x >= P:
                    m = m + 1
            if mm < m:
                mm = m
        print "Case #%d:"%i, mm
                
        
