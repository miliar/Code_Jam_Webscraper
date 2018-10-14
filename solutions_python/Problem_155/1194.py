#!/usr/bin/python
# coding=UTF-8

f=open("ovation_input_0.txt","r")

def solve(lp):
    nt=0
    nn=0
    add=0
    ov=0
    #print "==========="
    for x in range(len(lp)):
        nt+=lp[x]
    #print lp,len(lp)
    while nt>ov and nn<len(lp):
        ov=0
        #print nn
        for n in range(len(lp)):
            if n<=ov:
                ov+=lp[n]
            #print nn,add,ov,nt
        if ov!=nt:
            add+=1
            nt+=1
            lp[0]+=1
        else:
            break
        nn+=1
    return add

def readfileandsolve_ovation(f):
    for t in range(1, int(f.readline())+1):
        # Read testcase
        l=f.readline().strip();
        smax, lp = map(str, l.split(" "))
        smax=int(smax)
        lpp=[]
        for x in range(smax+1):
            lpp.append(int(lp[x]))
        # Solve testcase and output row
        print "Case #%d: %s" % (t, solve(lpp))
        
#############################################################

readfileandsolve_ovation(f)

