#!/usr/local/bin/python3.2
from sys import *

n = int(stdin.readline())

for case in range(n):
    n -= 1
    r1 = int(stdin.readline())-1
    mat1 = [int(x) for i in range(4) for x in stdin.readline().split()]
    r2 = int(stdin.readline())-1
    mat2 = [int(x) for i in range(4) for x in stdin.readline().split()]
    s1 = set(mat1[r1*4:r1*4+4])
    s2 = set(mat2[r2*4:r2*4+4])
    s = s1 & s2
    if len(s) == 0:
        print("Case #%d: Volunteer cheated!" % (case+1))
    elif len(s) > 1:
        print("Case #%d: Bad magician!" % (case+1))
    else:
        print("Case #%d: %d" % (case+1, s.pop()))