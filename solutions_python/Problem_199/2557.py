# -*- coding: utf-8 -*-
#
t = int(input())
#print("t=",3)
dbg = False   
#dbg = True
fout = open("a2.out", "w")
for i in range(1, t + 1):
    s, k = raw_input().split(" ") 
    k = int(k)
    s = [it for it in s]
    n = len(s)
    if dbg: print(k)
    if dbg: print(s)
    res = 0    
    
    for ind in range(0, n-k+1):
        if dbg: print("ind=",ind)
        if s[ind]=='-':
            for j in range(ind, ind+k):
                if s[j] == '+':
                    s[j] = '-'
                else:
                    s[j] = '+'
            if dbg: print("news=",s)
            res += 1
    if '-' in s:
        res = 'IMPOSSIBLE'
    
    fout.write("Case #{}: {}\n".format(i,res))

  