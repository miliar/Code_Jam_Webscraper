log2 = lambda x: math.log(x)/math.log(2)

T = input()
for t in range(T):
    N, K = map(int, raw_input().split())

    even = False
    K = map(int, list(bin(K)[2:][::-1]))
    for k in K:
        even = not N%2
        N = (N-1)/2

        if even and not k:
            N += 1

    print "Case #%d: %d %d"%(t+1, N+int(even), N)
