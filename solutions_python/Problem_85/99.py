#!/bin/python
import sys
import re
debug=False
def rl(f):
    return f.readline().strip()
def debugop(s):
    global debug
    if debug:
        print str(s)
if len(sys.argv) > 2:
    if sys.argv[2] == "yes":
        debug=True
f=open(sys.argv[1])
tcs=int(rl(f))
for i in range(0,tcs):
    vals=map(int,rl(f).split())
    l=vals[0]
    t=vals[1]
    n=vals[2]
    c=vals[3]
    di=vals[4:]
    dih={}
    for j in range(0,len(di)):
        k=0
        while True:
            if ((k*c)+j+1) >= n+1:
                break
            else:
                dih[str((k*c)+j) + str((k*c)+j+1)] = di[j]
                k=k+1
    debugop(dih)
    spd=0.5
    maxtime=0
    for j in range(0,n):
        maxtime = maxtime + dih[str(j)+str(j+1)]
    sorted_distances=sorted(dih.items(),key=lambda x:x[1])
    """    
    if t == 0:
        sorted_distances[0] = (sorted_distances[0][0],sorted_distances[0][1]/2)
        sorted_distances[1] = (sorted_distances[1][0],sorted_distances[1][1]/2)
        totdistance = 0
        for k,v in sorted_distances:
            totdistance = totdistance + v
        debugop("invoking special")
        print "Case #%d: %d" % (i+1,int(totdistance/0.5))
        continue
    if t >= maxtime:
        debugop("invoking special")
        print "Case #%d: %d" % (i+1,maxtime)
        continue
    """
    pos_till_t = t*0.5
    rmng = pos_till_t
    debugop("where=%f" % (pos_till_t))
    leftdistances=[]
    nowadding=False
    nonboostable=[]
    for j in range(0,n):
        dst = dih[str(j) + str(j+1)]
        if nowadding:
            leftdistances.append(float(dst))
            continue
        if (rmng - dst) > 0:
            nonboostable.append(dst)
            rmng = rmng - dst
            continue
        else:
            debugop("Nowadding:%d" % j)
            nonboostable.append(rmng)
            leftdistances.append(float(dst-rmng))
            nowadding = True
    leftdistances.sort(reverse=True)
    debugop(leftdistances)
    for j in range(0,l):
        leftdistances[j] = leftdistances[j]/2
    leftdistances = leftdistances + nonboostable
    debugop(leftdistances)
    debugop("l=%d , t=%d , n=%d" % (l,t,n))
    print "Case #%d: %d" % (i+1,reduce(lambda x,y:x+y,leftdistances)*2)
    
        
