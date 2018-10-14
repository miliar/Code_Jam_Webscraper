#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import collections
import copy

with open('./'+sys.argv[1], 'r+') as f:
    with open('./output.txt', 'w') as fout:

        line = f.readline()
        T = int(line)
        for n in range(T):
            numbers = f.readline().split()
            N = int(numbers[0])
            vals = []
            S=[(0,[])]
            possible_sums=[]
            for num in [int(numbers[i+1]) for i in range(len(numbers)-1)]:
                vals.append(num)
            summ=0
            #print vals
            fout.write("Case #"+str(n+1)+":\n")
            for val in vals:     
                S2=S[:] 
                #print S2
                for i in range(len(S2)):
                    (s,sset) = S2[i]
                    #print (s, sset)
                    sset2=sset[:]
                    sset2.append(val)
                    #print sset2
                    sum_temp = s+val
                    S.append((sum_temp, sset2))
                    #print S
                    if sum_temp in possible_sums:
                        summ=sum_temp
                        break
                    else:
                        possible_sums.append(sum_temp)
                if summ:
                    #print S
                    break
                #print S
            if summ:
                s1=False
                for (s,sset) in S:
                    if s==summ and not s1:
                        S1=sset
                        s1=True
                    elif s==summ:
                        S2=sset
                set1=''
                for val in S1:
                    set1+=str(val)+' '
                fout.write(set1.rstrip()+"\n")
                set2=''
                for val in S2:
                    set2+=str(val)+' '
                fout.write(set2.rstrip()+"\n")
            else:
                fout.write("Impossible\n")
            #exit(0)
        
