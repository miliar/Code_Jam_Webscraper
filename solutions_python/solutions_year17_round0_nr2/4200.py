# -*- coding: utf-8 -*-
"""
Created on Sat Apr 08 12:16:54 2017

@author: maxim
"""

nf= "B-large.in"

from bibliperso import * 
t = get_lines(nf)
T = int(t[0])
k = 1 


def sol(N):
    l = len(N) - 1
    #print(l)
    fin = l
    rep = ['9'for i in range(l+1)]
    i = 0 
    #print("fin " + str(fin))
    while( fin > 0 and  i <= fin-1):
        #print('fin ' + str(fin) + 'i ' + str(i))
        if(N[i] <= N[i+1]):
            i += 1
        else: 
            N = str(int(N[:i+1]) - 1)
            fin = i 
            i = 0
    for i in range(fin+1):
        if(i == 0 and N[i] == '0'):
            rep[i] = ''
        else : 
            rep[i] = N[i]
    rep = ''.join(rep)
    return rep 

rep=""
for i in range(T):
    rep += "Case #{}: {}\n".format(i+1,sol(t[i+1]))
    
write_in('tidylarge.txt',rep)
