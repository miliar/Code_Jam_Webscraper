# large dataset version
# Python 2.7.2
import sys

stdin = sys.stdin.readlines()
cases = int(stdin.pop(0))
for i in xrange(cases):
    possible = True
    rc = stdin.pop(0).split()
    rownum = int(rc[0])
    colnum = int(rc[1])
    lawnrows = []
    for j in xrange(rownum):
        lawnrows.append([])
        for k in stdin.pop(0).split():
            lawnrows[-1].append(int(k))
    lawncols = []
    for j in xrange(colnum):
        lawncols.append([])
        for k in xrange(rownum):
            lawncols[j].append(lawnrows[k][j])
    for j in xrange(rownum):
        for k in xrange(colnum):
            if lawnrows[j][k] < max(lawnrows[j]) and lawnrows[j][k] < max(lawncols[k]):
                possible = False
    if possible:
        print "Case #"+str(i+1)+": YES"
    else:
        print "Case #"+str(i+1)+": NO"
