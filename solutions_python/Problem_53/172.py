T = int(raw_input())

for c in range(1,T+1):
    N,K = map(int, raw_input().split())
    N = pow(2,N)
    
    light = "OFF"
    if K%N == N-1: 
        light = "ON"
        
    print "Case #%d: %s"%(c, light)