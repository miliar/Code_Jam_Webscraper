# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 11:37:50 2017

@author: Emad Yehya
"""

fi = file('A-large.in', 'r')
fo = file('out.txt', 'w')

T = int(fi.readline()[:-1])


def solve_for_str(S, k):
    ans = 0
    P = [S[i] == '+' for i in range(0, len(S))]
#    print P
    for i in range(0, len(P) - k + 1):
        if(not P[i]):
            ans += 1
            for j in range(i, i+k):
                P[j] = not P[j]
                
    first_in_list = P[len(P) - k]
    for i in range(len(P) - k, len(P)):
        if(P[i] != first_in_list):
            return "IMPOSSIBLE"
    else: 
        return str(ans)
    
    
t= 0
for t in range(1, T+1):
#while(True):
    line = fi.readline()[:-1]
#    line = raw_input()
    S = line.split(' ')[0]
    k = int(line.split(' ')[1])
#    find first break, if any
    print "Case #" + str(t) + ": "+ solve_for_str(S, k)
    fo.write("Case #" + str(t) + ": "+ solve_for_str(S, k) + "\n")
    
fi.close()
fo.close()