#!/usr/bin/env python

'''
Input 
 	
Output 
 
3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1

Case #1: 6
Case #2: 100
Case #3: 4
'''



def do(seq):
    b=1
    o=1
    ctr=0
    
    ctrNow=0
    isTurnChanged=False
    turn=None
    
    for i in seq:
        #print i
        
        if turn == None:
            turn=i[0]
        
        if i[0]==turn: isTurnChanged=False
        else: isTurnChanged=True
        
        turn=i[0]
        
        if turn=='O':
            diff=abs(i[1]-o)
            o=i[1]
        else:
            diff=abs(i[1]-b)
            b=i[1]
        
        if not isTurnChanged:
            ctrNow+=diff+1
        else:
            ctr+=ctrNow
            #print 'ctr',ctr
            if diff <= ctrNow:
                ctrNow=1
            else:
                ctrNow=diff-ctrNow+1


    ctr+=ctrNow
    return ctr

###seq=[("O",2),("B",1),("B",2),("O",4)]
####seq=[("O",5),("O",8),("B",100)]
####seq=[("B",2),("B",1)]
###
###print 'result', do(seq)

import sys
fname=sys.argv[1]

input=[]
f=open(fname,'r')
fout=open(fname+'.out','w')
numLine=int(f.readline())
for num in xrange(1,numLine+1):
    line=f.readline().strip()
    raw=line.split()
    input=[]
    
    for i in xrange(1,len(raw),2):
        #print i
        input.append((raw[i],int(raw[i+1])))
    
    #if input[0]!=len(input[1:]):
    #    print "wrong format", input
    
    print 'Case #'+`num`+': '+`do(input)`
    fout.write('Case #'+`num`+': '+`do(input)`+'\n')
fout.close()

