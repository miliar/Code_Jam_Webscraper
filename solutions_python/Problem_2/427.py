#!/usr/bin/python

import sys
import re
from bisect import bisect
from collections import defaultdict

evts = defaultdict(list)
times = []
t = -1
trains = {"A":0,"B":0}
needed = {"A":0,"B":0}

def f(ta,tb):
    global evts,times,t,trains,needed
    evts = defaultdict(list)
    times = []
    trains = {"A":0,"B":0}
    needed = {"A":0,"B":0}
    for (sh,sm,fh,fm) in ta:
        st = sh*60 + sm
        ft = fh*60 + fm
        insert_evt(st,"DA")
        insert_evt(ft,"AB")
    for (sh,sm,fh,fm) in tb:
        st = sh*60 + sm
        ft = fh*60 + fm
        insert_evt(st,"DB")
        insert_evt(ft,"AA")
    for x in evts.values():
        x.sort(mysort)
    simulate()
    return "%s %s" % (needed["A"],needed["B"])

def mysort(x,y):
    global evts,times,t,trains,needed
    if x[0] == "R":
        if y[0] != "R":return -1
        else:return 0
    if x[0] == "D":
        if y[0] != "D":return 1
        else:return 0
    raise ValueError()

def insert_evt(time,evt):
    global evts,times,t,trains,needed
    #Ax = Arival at x
    #Dx = Departure at x
    #Rx = train Ready at x
    if evt[0] == "A":
        insert_evt(time + t,"R%s" % evt[1])
        return
    p = bisect(times,time)
    if p == 0 or times[p-1] != time:
        times.insert(p,time)
    evts[time].append(evt)

def simulate():
    global evts,times,t,trains,needed
    for time in times:
        currevts = evts[time]
        for ev in currevts:
            if ev[0] == "R":
                trains[ev[1]] = trains[ev[1]] + 1
            elif ev[0] == "D":
                if(trains[ev[1]] == 0):
                    trains[ev[1]] = 1
                    needed[ev[1]] = needed[ev[1]] + 1
                trains[ev[1]] = trains[ev[1]] - 1
            else:
                raise ValueError()

if __name__ == "__main__":
    infile = sys.argv[1]
    lines = open(infile)
    n = lines.next()
    for i in range(int(n.rstrip())):
        t = int(lines.next().rstrip())
        na,nb = map(int,lines.next().rstrip().split(" "))
        ta = []
        for j in range(na):
            m = re.match(r"(\d\d):(\d\d) (\d\d):(\d\d)",lines.next().rstrip())
            (h1,m1,h2,m2) = m.groups()
            ta.append(map(int,(h1,m1,h2,m2)))
        tb = []
        for j in range(nb):
            m = re.match(r"(\d\d):(\d\d) (\d\d):(\d\d)",lines.next().rstrip())
            (h1,m1,h2,m2) = m.groups()
            tb.append(map(int,(h1,m1,h2,m2)))
        print "Case #%i: %s" % (i+1,f(ta,tb))