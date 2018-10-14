def readint(): return int(raw_input())
def readarray(f): return map(f,raw_input().split())

T = readint()

for t in xrange(T):
    N,K = readarray(int)
    flg = 'OFF'
    if K >= 2**N-1 and (K+1)%(2**N)==0:
        flg = 'ON'
    print "Case #%d: %s" % (t+1,flg)
                
