#!/usr/bin/env python

# Google code jam 2012

import sys

puiss10 = []
g_dic = []

def recycl(x,i,m):
    return x//puiss10[i] + (x % puiss10[i])*puiss10[m-i]

# s : surprises
# p : threshold
def result(a,b):
    count = 0
    m = len(str(a))

    for k in range(a,b+1):
        dic = {}
        for j in range(1,m):
            if k not in g_dic[j]:
                r = recycl(k,j,m)
                g_dic[j][k] = r
            else:
                r = g_dic[j][k]

            if r > k and r >= a and r <= b:
                if not (r,k) in dic:
                    count += 1
                    dic[(r,k)] = 1

    return str(count) 



for k in range(10):
    puiss10.append(10**k)
    g_dic.append({})
    
p = int(sys.stdin.readline())
for s in range(1,p+1):
    l = []
    line = sys.stdin.readline()

    a,_,line = line.partition(' ')
    a = int(a)
    b,_,line = line.partition(' ')
    b = int(b)

    print("Case #" + str(s) + ": " +  result(a,b))

