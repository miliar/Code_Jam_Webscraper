# Author: Dan Kunkle (kunkle@gmail.com)

import sys
import os
import sets
import re
import math

def solve(engs, searches):
    C = [];
    C.append([0] * len(engs));
    for n in range(len(searches)):
        C.append([float("inf")] * len(engs));
        for s in range(len(engs)):
            best = float("inf");
            for t in range(len(engs)):
                if not searches[n] == engs[t]:
                    val = C[n][t] + (1 * (not t == s));
                    best = min(best, val);
            C[n+1][s] = best;
    return min(C[len(searches)]);

def doOne(fin):
    engs = [];
    searches = [];
    nEngs = int(fin.readline().strip());
    for i in range(nEngs):
        engs.append(fin.readline().strip());
    nSearches = int(fin.readline().strip());
    for i in range(nSearches):
        searches.append(fin.readline().strip());
    return solve(engs, searches);

def run(caseName):
    fnin = caseName + ".in";
    fnout = caseName + ".out";
    fin = open(fnin);
    fout = open(fnout, 'w');
    fout.truncate(0);
    ncases = int(fin.readline().split()[0]);
    for case in range(ncases):
        ans = "Case #" + str(case+1) + ": " + str(doOne(fin));
        print ans;
        fout.write(ans + "\n");
    fin.close();
    fout.close();
