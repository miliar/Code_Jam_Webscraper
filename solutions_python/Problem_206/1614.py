# Google codejam 2017B
# A. 

for t in range(1, int(input()) + 1):
    D, N = map(int, input().split())
    K = []
    S = []
    inputs = []
    for _ in range(N):
        k, s = map(int, input().split())
        inputs.append((k, s))
    inputs.sort()
    K, S = zip(*inputs)

    result = D / ((D - K[0]) / S[0])
    if N > 1:
        ctime = (K[0] - K[1]) / (S[1] - S[0]) if S[1] != S[0] else 0
        cpoint = K[0] + S[0]*ctime
        #print(ctime, cpoint)
        if ctime > 0 and cpoint < D:
            #print(D - cpoint, S[0], S[1])
            result = D / (ctime + ((D - cpoint) / S[1]))

    print ("Case #{}: {}".format(t, result))
