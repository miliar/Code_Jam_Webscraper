#! /usr/bin/env python

import sys
fin = open(sys.argv[1], "r")
fout = open("A.out", "w")

T = int(fin.readline())

for i in range(T):
    N = int(fin.readline())
    s = str(N)
    d = []
    change=0
    s2 = ""
    for digit in s:
        d.append (int(digit))
    #print (d)
    for j in range(0, len(d)-1):
        if d[j]>d[j+1]:
            for k in range(j, len(d)-1):
                d[k+1]=0
                #print(d)
            change=1
            l=j
            if l>=0:
                while (d[l]<=d[l-1] and l!=0):
                    d[l]=0
                    if l>=1:
                        l=l-1
            break
    #print(d)
    if change == 0:
        ans = N
    else:
        for digit in d:
            s2 = s2+ str(digit)
        ans = int(s2)-1
    print(ans)    
    fout.write("Case #" + str(i+1) + ": ")
    fout.write(str(ans) + "\n")
    

