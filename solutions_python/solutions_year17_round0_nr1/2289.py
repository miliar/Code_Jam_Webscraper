N = int(input())
for i in range(N):
    S, K = input().split()
    K = int(K)
    S = list(map(lambda x: x == "+",S))
    M = len(S)
    count = 0
    for t in range(0, M - K + 1):
        if not S[t]:
            count += 1 
            for current in range(t, t+K):
                S[current] = not S[current]
    if all(S):
        print("Case #%d: %d"%(i+1,count))
    else :
        print ("Case #%d: IMPOSSIBLE"%(i+1))
