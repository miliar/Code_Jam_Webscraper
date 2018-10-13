#!\bin\python
#encoding UTF-8
#solution2.py

import string
import linecache

inname = "B-small-attempt0.in"
outname = inname.rstrip(".in") + ".out"
fin = open(inname, "r")
fout = open(outname, "w")

allCaseNum = int(linecache.getline(inname, 1).rstrip("\n"))
caseNum = 0
base = 2

for caseNum in xrange(1, allCaseNum+1):
    val = linecache.getline(inname, caseNum+1).rstrip("\n").split( )
    print val
    C = float(val[0])
    F = float(val[1])
    X = float(val[2])
    totalTime = X
    totalTimeNext = X/base
    farm = 0
    while totalTime >= totalTimeNext:
        farm = farm + 1
        totalTime = totalTimeNext
        totalTimeNext = 0
        for i in range(0, farm):
            totalTimeNext = totalTimeNext + C/(base+i*F)
        totalTimeNext = totalTimeNext + X/(base+farm*F)
    answer = "Case #%s: %s\n" %(caseNum, totalTime)
    fout.write(answer)
fin.close()
fout.close()