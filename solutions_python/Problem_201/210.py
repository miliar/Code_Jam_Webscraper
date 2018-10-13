def compute(N, K):
    length = N
    long, short = 1, 0

    while 2*(long + short) <= K:
        if length % 2 == 1:
            long = 2*long + short
        else:
            short = 2*short + long
        length = length // 2

    if K > 2*long+short-1:
        length -= 1
    return (length // 2, (length-1) // 2)
        

T = int(input())
for t in range(1, T+1):
    N, K = [int(x) for x in input().split()]

    M, m = compute(N, K)
    print("Case #%d: %d %d"%(t,M,m)) 
