T = int(raw_input())

for i in range(T):
    N, K = map(int, raw_input().split())
    
    print "Case #%d:" % (i+1),
    
    if K % (2**N) == (2**N)-1: print "ON"
    else: print "OFF"
