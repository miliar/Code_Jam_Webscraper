'''
Created on Apr 13, 2013

@author: Colin Lee
'''
import sys

def worker(c,r,w,h):
    for x in range(w):
        for y in range(h):
            p=c[x][y]
            av1=False
            av2=False
            for z in c[x]:
                if p<z:
                    av1=True
                    break
            for z in r[y]:
                if p<z:
                    av2=True
                    break
            
            if av1 and av2:return 'NO'
    return 'YES'
sys.stdin=open('B-large.in')
sys.stdout=open('B-large.out','w')
for _ in range(int(input())):
    c=[]
    r=[]
    h,w=[int(x) for x in input().strip().split()]
    for x in range(h):
        r.append([int(x) for x in input().strip().split()])
    c=list(map(list,zip(*r)))
    print('Case #'+str(_+1)+': '+worker(c,r,w,h))