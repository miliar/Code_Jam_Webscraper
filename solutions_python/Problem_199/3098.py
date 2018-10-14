T = int(input())

for t in range(T):
    temp = input().split()
    S = [True if c == '+' else False for c in temp[0]]
    K = int(temp[1])
    fCount = 0
    for p in range(len(S) - K + 1):
        if not S[p]:
            fCount += 1
            for i in range(K):
                S[p + i] = not S[p + i]
    if all(S):
        print("Case #" + str(t + 1) + ": " + str(fCount))
    else:
        print("Case #" + str(t + 1) + ": IMPOSSIBLE")
