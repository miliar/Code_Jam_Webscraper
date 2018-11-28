# Author: Dan Kunkle (kunkle@gmail.com)

import sys
import os
import sets
import re
import math

def t2m(t):
    h, m = map(int, t.split(':'));
    return h*60 + m;

def nTrains(arv, dep):
    arv.sort();
    dep.sort();
    n = 0;
    maxN = 0;

    while(len(arv) and len(dep)):
        if(arv[0] == dep[0]):
            arv.pop(0);
            dep.pop(0);
            continue;
        if(arv[0] < dep[0]):
            n -= 1;
            arv.pop(0);
        else:
            n += 1;
            dep.pop(0);
        maxN = max(maxN, n);
    maxN = max(maxN, n + len(dep));
    return max(maxN, 0);

def doOne(fin):
    turnT = int(fin.readline().strip());
    nA, nB = tuple(map(int, fin.readline().split()));
    depA = [];
    arvA = [];
    depB = [];
    arvB = [];
    for i in range(nA):
        da, ab = tuple(map(t2m, fin.readline().split()));
        depA.append(da);
        arvB.append(ab+turnT);
    for i in range(nB):
        db, aa = tuple(map(t2m, fin.readline().split()));
        depB.append(db);
        arvA.append(aa+turnT);
    return (nTrains(arvA, depA), nTrains(arvB, depB));

def run(caseName):
    fnin = caseName + ".in";
    fnout = caseName + ".out";
    fin = open(fnin);
    fout = open(fnout, 'w');
    fout.truncate(0);
    ncases = int(fin.readline().split()[0]);
    for case in range(ncases):
        a, b = doOne(fin);
        ans = "Case #%d: %d %d" % (case+1, a, b);
        print ans;
        fout.write(ans + "\n");
    fin.close();
    fout.close();
