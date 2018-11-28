# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 01:31:02 2017

@author: Yenyu
"""

txtin="B-large.in"
foutn="B-out.txt"
f = open(txtin,'r')
T=int(f.readline())

with open(foutn, 'w') as fout:
    for case in range(T):
        N=f.readline()
        N=int(N)
        def isittidyfunction(x):
            coll=x
            array=[]
            n=0
            while coll>0:
                array.append(coll)               
                coll=coll//10
                n=n+1
            numbers=[array[-1]]
            for i in range(n-1):
                numbers.append(array[-2-i]-array[-1-i]*10)
            res=True
            for l in range(n-1):
                if numbers[l]>numbers[l+1]:
                    res=False
                    break
            return res
        finding=True
        while finding:
            if isittidyfunction(N):
                answer=N
                finding=False
            else:
                coll=N
                array=[]
                n=0
                while coll>0:
                    array.append(coll)               
                    coll=coll//10
                    n=n+1
                numbers=[array[-1]]
                for i in range(n-1):
                    numbers.append(array[-2-i]-array[-1-i]*10)
                for l in range(n-1):
                    if numbers[l]>numbers[l+1]:
                        numbers[l]=numbers[l]-1
                        for k in range(n-l-1):
                            numbers[l+k+1]=9
                for j in range(n):
                    numbers[-j-1]=numbers[-j-1]*pow(10, j)
                N=0
                for add in range(n):
                    N=N+numbers[add]
        print (answer)
        fout.write('Case #'+str(case+1)+': '+str(answer)+'\n')                
print ('Fin')

                