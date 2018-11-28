import sys
from sets import Set

def ReadInts():
    return list(map(int, sys.stdin.readline().strip().split(" ")))

outputFormat = "Case #%d: %d"

pathList = Set([])
def insertDir(path):
    ret = 0
    l = path[1:].split("/")

    tp = "/"
    for p in l:
        tp = tp + p
        if tp not in pathList:
            ret = ret + 1
            pathList.add(tp)
            
    return ret

C = ReadInts()[0]
for case in xrange(1, C+1):
    (N,M) = ReadInts()

    pathList = Set([])
    for _ in xrange(N):
        insertDir(sys.stdin.readline().strip())

    cnt = 0
    for _ in xrange(M):
        cnt = cnt + insertDir(sys.stdin.readline().strip())

    print outputFormat % (case, cnt)
