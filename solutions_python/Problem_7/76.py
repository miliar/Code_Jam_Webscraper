# Author: Dan Kunkle (kunkle@gmail.com)

import sys
import os
import re
import math

# input shortcuts
def lis(fin): return fin.readline().split();
def lis1(fin): return fin.readline().split()[0];
def lii(fin): return map(int, fin.readline().split());
def lii1(fin): return map(int, fin.readline().split())[0];

def calcPts(n, A, B, C, D, x0, y0, M):
    pts = [(x0, y0)];
    X = x0;
    Y = y0;
    for i in range(1,n):
        X = (A * X + B) % M;
        Y = (C * Y + D) % M;
        pts.append((X,Y));
    return pts;

def cent(pts, i, j, k):
    return ((pts[i][0] + pts[j][0] + pts[k][0])/3.0, \
            (pts[i][1] + pts[j][1] + pts[k][1])/3.0);

# give it a whack
def doOne(fin):
    n, A, B, C, D, x0, y0, M = lii(fin);
    pts = calcPts(n, A, B, C, D, x0, y0, M);
    
    ans = 0;
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i<j and j<k:
                    c = cent(pts,i,j,k);
                    if c[0] == int(c[0]) and c[1] == int (c[1]):
                        ans += 1;
    return str(ans);

# drive it
def run(caseName):
    fnin = caseName + ".in";
    fnout = caseName + ".out";
    fin = open(fnin);
    fout = open(fnout, 'w');
    fout.truncate(0);
    ncases = int(fin.readline().split()[0]);
    for case in range(ncases):
        ans = doOne(fin);
        ans = "Case #%d: %s" % (case+1,ans);
        print ans;
        fout.write(ans + "\n");
    fin.close();
    fout.close();
