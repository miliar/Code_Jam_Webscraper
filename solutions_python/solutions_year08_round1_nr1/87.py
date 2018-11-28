# Author: Dan Kunkle (kunkle@gmail.com)

import sys
import os
import sets
import re
import math

def doOne(fin):
    n = int(fin.readline().split()[0]);
    x = sorted(map(int, fin.readline().split()));
    y = list(reversed(sorted(map(int, fin.readline().split()))));
    ans = sum([x[i]*y[i] for i in range(len(x))]);
    return ans;

def run(caseName):
    fnin = caseName + ".in";
    fnout = caseName + ".out";
    fin = open(fnin);
    fout = open(fnout, 'w');
    fout.truncate(0);
    ncases = int(fin.readline().split()[0]);
    for case in range(ncases):
        n = doOne(fin);
        ans = "Case #%d: %d" % (case+1, n);
        print ans;
        fout.write(ans + "\n");
    fin.close();
    fout.close();
