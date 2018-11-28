import os
from collections import defaultdict
__author__ = 'steven'

question='qd'
fs={'t1','-small','-large.in'}

def getGameTypeA(l1,l2):
    print "****"
    print l1
    print l2
    ablist=list()
    while 1:
        if l1[0]>l2[0]:
            ablist.append('a');
            l1.pop(0);
        else:
            ablist.append('b');
            l2.pop(0);
        if len(l1)*len(l2)==0:
            break

    for i in range(0,len(l2)):
        ablist.append('b')
    for i in range(0,len(l1)):
        ablist.append('a')

    fcount=0
    scount=0
    print ablist
    while len(ablist)>0:
        #print ablist
        if ablist[-1]=='a':
            fcount+=1
            ablist.pop()
            ablist.pop(ablist.index('b'))
        else:
            scount+=1
            ablist.pop(len(ablist)-ablist[::-1].index('a')-1)
            ablist.pop()
    return scount








def getGameTypeB(l1,l2):
    awin=0
    bwin=0
    while len(l1)>0:
        l=len(l1)-1;
        if l1[0]>l2[0]:
            awin+=1
            l1.pop(0);
            l2.pop()
        else:
            l2.pop(0)
            l1.pop(0)
    return awin
def solver(l1,l2):

    return getGameTypeA(list(l1),list(l2)),getGameTypeB(list(l1),list(l2))



for s in fs:
    print question+s
    f='./'+question+s
    if os.path.isfile('./'+question+s):
        ls=open(f)
        noq=(int)(ls.readline())
        fout=open(question+s+'-a','w')
        print noq
        for i in range(0,noq):
            noc=(int)(ls.readline())
            l1=ls.readline().split()
            l1=sorted([float(s) for s in l1], reverse=True)
            l2=ls.readline().split()
            l2=sorted([float(s) for s in l2], reverse=True)
           # print l1
           # print l2
            s=solver(l1,l2)
            fout.write('Case #%d: %d %d\n'%(i+1,s[0],s[1]))



