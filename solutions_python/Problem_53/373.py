def readint(): return int(raw_input())
def readlinearray(typecast): return map(typecast, raw_input().split())

def ison(N, K):
    return (K+1) % (2**N) == 0

N = readint()
for i in range(N):
    (N, K) = readlinearray(int)
    if ison(N, K):
        res = "ON"
    else: res = "OFF"
    print "Case #%d: %s" % (i + 1, res)
    
