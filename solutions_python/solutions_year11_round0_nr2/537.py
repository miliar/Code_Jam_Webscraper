# -*- coding: utf-8 -*-
import sys
nfh = sys.argv[0][:-3];
nfhin = nfh + ".in"; nfhout= nfh + ".out";
fin = open(nfhin, "r"); fout= open(nfhout,"w");
def rl(): global fin; return fin.readline()[:-1];
def out(cnum, outs): global fout; fout.write("".join(["Case #",str(cnum),": ",str(outs),"\n"]));
def end(): global fout; fout.close();

def analyse(l, opposed, transform):
    if len(l) > 1:
        x = l[-1]
        a = l[-2]
        b = l[-1]
        if a+b in transform:
            l = l[:-2]
            l.append(transform[a+b])
        elif b+a in transform:
            l = l[:-2]
            l.append(transform[b+a])
        elif (x in opposed) and len(opposed[x].intersection(set(l[:-1])))>0:
            l = []

    return l

# --- program ---
def main(p):
    cels = []
    dels = []
    i = 0
    c = int(p[i])
    for cc in xrange(c):
        i+=1
        cels.append(p[i])
    i+=1
    d = int(p[i])
    for dd in xrange(d):
        i+=1
        dels.append(p[i])
    els = p[-1]

    #prepare
    opposed = dict()
    for x in dels:
        a = x[0]
        b = x[1]
        if a not in opposed:
            opposed[a] = set()
        if b not in opposed:
            opposed[b] = set()
        opposed[b].add(a)
        opposed[a].add(b)

    transform = dict()
    for x in cels:
        a = x[0]
        b = x[1]
        c = x[2]
        transform[a+b] = c
        transform[b+a] = c

    l = []
    for x in els:
        l.append(x)
        oldl = list(l)
        while True:
            l = analyse(l, opposed, transform)
            if l == oldl:
                break
            oldl = list(l)

    return repr(l).replace("'","")

# --- test configuration ---
NT = int(rl());
for T in xrange(1, NT+1):
    param = rl().split(" ")
    res = main(param)
    out(T,res)
end()
