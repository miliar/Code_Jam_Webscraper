import sys

T = int(sys.stdin.readline())
for case in xrange(1, T+1):
    N, M = map(int, sys.stdin.readline().split())
    array = []
    for _ in xrange(N):
        l = map(int, sys.stdin.readline().split())
        array.append(l)
    
    ok = True
    
    for x in xrange(N):
        for y in xrange(M):
            sub_ok1 = True
            for i in xrange(M):
                if array[x][i] > array[x][y]:
                    sub_ok1 = False
            
            sub_ok2 = True
            for i in xrange(N):
                if array[i][y] > array[x][y]:
                    sub_ok2 = False
            
            if not (sub_ok1 or sub_ok2):
                ok = False
            
    def result(ok):
        if ok:
            return "YES"
        return "NO"
    print "Case #"+str(case)+": "+result(ok)
