import sys
import math
import psyco
psyco.full()

fin=open('input.txt','r')
fout=open('output.txt','w')

l=int(fin.readline())
for case in range(l):
    lcount=int(fin.readline())
    lines=[]
    for i in range(lcount):
        lines.append(fin.readline().strip())
    lrightmost=[i.rfind('1') for i in lines]
    cost=0
    for i in range(lcount):
        for j in range(len(lrightmost)):
            if lrightmost[j]<=i:
                break
        #Move j to i
        cost+=j
        del lrightmost[j]
    
    fout.write("Case #%d: %d\n"%(case+1,cost))
    print case
 
fin.close()
fout.close()
