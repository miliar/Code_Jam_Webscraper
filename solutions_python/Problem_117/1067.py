import cStringIO
from sys import stdin

def removeRow(lawn, ii):
    lawn.pop(ii)

def removeColumn(lawn, jj):
    for row in lawn:
        row.pop(jj)

def checkPattern(lawn):
    if len(lawn) == 1 or len(lawn[0]) == 1:
        return True

    hmin = lawn[0][0]
    ii = None
    jj = None
    for i in xrange(len(lawn)):
        equal = True
        for j in xrange(len(lawn[0])):
            if lawn[i][j] != lawn[i][0]:
                equal = False
            if lawn[i][j] < hmin:
                hmin = lawn[i][j]
        if equal and lawn[i][0] == hmin:
            ii = i
    if ii!=None and lawn[ii][0] != hmin:
        ii = None

    for j in xrange(len(lawn[0])):
        if lawn[0][j] > hmin:
            continue
        equal = True
        for i in xrange(len(lawn)):
            
            if lawn[i][j] != lawn[0][j]:
                equal = False
            if lawn[i][j] < hmin:
                hmin = lawn[i][j]
        if equal and lawn[0][j] == hmin:
            jj = j

    if jj == None and ii == None:
        return False

    elif jj != None and ii != None:
        if lawn[ii][0] <= lawn[0][jj]:
            removeRow(lawn, ii)
            return checkPattern(lawn)
        else:
            removeColumn(lawn, jj)
            return checkPattern(lawn)
    elif ii != None:
        removeRow(lawn, ii)
        return checkPattern(lawn)
    else:
        removeColumn(lawn, jj)
        return checkPattern(lawn)

T = int(raw_input())
all = cStringIO.StringIO(stdin.read())

for t in xrange(T):
    N, M = map(int, all.next().split())
    lawn = []
    for n in xrange(N):
        lawn.append(map(int, all.next().split()))
    
    res = checkPattern(lawn)
    if res:
        print 'Case #'+ str(t+1) +': YES'
    else:
        print 'Case #'+ str(t+1) +': NO'
