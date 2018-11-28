#!/usr/bin/env python
import sys
import os
import math
def to_key(c):
    if c == " ":
        return "0"
    elif c <= "r":
        key = (ord(c) - ord("a"))/3 + 2 
        times = (ord(c) - ord("a"))%3 + 1 
        return "".join(str(key) for i in range(times))
    elif c == "s":
        return "7777"
    elif c == "z":
        return "9999"
    else:
        key = (ord(c) - ord("t"))/3 + 8 
        times = (ord(c) - ord("t"))%3 + 1 
        return "".join(str(key) for i in range(times))

with open(sys.argv[1], "r") as input:
    data = input.readlines()
with open("%s.result" % sys.argv[1], "w") as output:
    n = int(data[0])
    for i in range(n):
        string = data[i+1][1:-1].split()
        olist=[]
        blist=[]
        slist=[]
        for j, v in enumerate(string):
            if v == "O":
                olist.append(int(string[j+1]))
                slist.append(0)
            elif v == "B":
                blist.append(int(string[j+1]))
                slist.append(1)
        oi = 1
        bi = 1
        time = 0
        for k in slist:
            if k == 0:
                if len(olist) == 0:
                    continue
                else:
                    ot = olist.pop(0)
                    steps = math.fabs(ot - oi) + 1
                    time += steps
                    oi = ot
                    if len(blist) == 0:
                        continue
                    bt = blist[0]
                    if math.fabs(bt - bi) < steps:
                        bi = bt
                    else:
                        if math.fabs(bt - bi - steps) < math.fabs(bt - bi + steps):
                            bi += steps
                        else:
                            bi -= steps
            elif k == 1:
                if len(blist) == 0:
                    continue
                else:
                    bt = blist.pop(0)
                    steps = math.fabs(bt - bi) + 1
                    time += steps
                    bi = bt
                    if len(olist) == 0:
                        continue
                    ot = olist[0]
                    if math.fabs(ot - oi) < steps:
                        oi = ot
                    else:
                        if math.fabs(ot - oi - steps) < math.fabs(ot - oi + steps):
                            oi += steps
                        else:
                            oi -= steps
        print>> output,  "Case #%d: %d" % (i + 1, time)
        print "Case #%d: %d" % (i + 1, time)
