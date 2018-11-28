# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 05:07:47 2017

@author: Tom
"""
import math
fname = 'A-large.in'
oname = fname[:-3]+'.out'
with open(fname,'r') as f:
    with open(oname,'w') as o:
        T = int(f.readline().strip())
        for case in range(1,T+1):
            N,K = list(map(int,f.readline().strip().split()))
            print('Case {}: {},{}'.format(case,N,K))
            P = []
            for p in range(N):
                r,h = list(map(int,f.readline().strip().split()))
                atop = r*r
                aside = 2*r*h
                P.append([p,r,h,aside,atop+aside])
            Pside = sorted(P,key=lambda p:p[3],reverse=True)
            Pall = sorted(P,key=lambda p:p[4],reverse=True)
            print(P)
            bestArea = 0
            bestList = []
            # try starting with largest area pancake on bottom
            for bot in Pall:
                # try to assemble pancakes on top of it
                thisArea = bot[4]
                thisList = [bot]
                num = 1
                for mid in Pside:
                    if num == K:
                        break
                    if mid[0] != bot[0] and mid[1] <= bot[1]:
                        thisArea = thisArea + mid[3]
                        num = num + 1
                        thisList.append(mid)
                if num < K:
                    print('Not enough pancakes selected.')
                elif thisArea > bestArea:
                    print('Found new best: ' + str(thisArea))
                    print(thisList)
                    bestList = thisList
                    bestArea = thisArea
                else:
                    print('Discarded ' + str(thisArea))
            print([p[0] for p in bestList])
                
            o.write('Case #{}: {:.7f}\n'.format(case,bestArea*math.pi))
                            
            
            