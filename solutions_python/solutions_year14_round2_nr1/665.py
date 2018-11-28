#! /opt/local/bin/python
from numpy import *
from itertools import *
#from gmpy2 import *
#f=open('test1')
f=open('A-small-attempt3.in')
#f=open('A-large.in')
def uniq(seq):
    b=''
    lastchar='lambda'
    i=0
    for c in seq:
        if c!=lastchar:
            lastchar=c
            b=b+lastchar
    return b
def tup(seqs):
    b=[]
    for seq in seqs:
        #tmpuniq=uniq(seq)
        a=[]
        lastchar='lambda'
        i=0
        for c in seq:
            if c == lastchar:
                a[-1] += 1
            else:
                lastchar = c
                a = a +[1]
        b=b+[a]
    return b



T=int(f.readline())
for tt in range(1,T+1):
    N=int(f.readline())
    s=[]
    for n in range(N):
        s=s+[f.readline().strip()]
    flag= False
    tmp=uniq(s[0])
    for i in range(1,N):
        #print tmp,uniq(s[i])
        if tmp != uniq(s[i]):
            print 'Case','#'+str(tt)+':','Fegla Won'
            flag = True
            continue
    if flag==True:
        continue
    tpls=array(tup(s))
    #print tmp,tpls

    dst =  sum([abs(tpls[0][j]-tpls[1][j]) for j in range(len(tpls[0]))])
    print 'Case','#'+str(tt)+':',dst
    #for i in range(len(tmp)):
    #    min_i=min(tpls[:,i])
    #    max_i=max(tpls[:,i])
    #    tmplst=tmplst+[range(min_i,max_i+1)]
    ##print tmplst
    #mindist=99999
    #for element in product(*tmplst):
    #    dst=0
    #    for i in range(N):
    #        dst +=  sum([abs(element[j]-tpls[i][j]) for j in range(len(tmp))])
    #    if dst<mindist:
    #        mindist=dst
    #print 'Case','#'+str(tt)+':',mindist

