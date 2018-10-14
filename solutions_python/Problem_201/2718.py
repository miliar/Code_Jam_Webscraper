def solve(N, K):
    Q = list([1])
    for i in range(1, N+1):
        Q.append(0)
    Q.append(1)
    index = int(len(Q)/2)
    Q[index] = 1
    Min = N
    Max = 0
    K = K - 1
    last = index
    while True:
        if K == 0:
            L = 0
            R = 0
            for i in reversed(range(0, last)):
                if Q[i] == 1:
                    L = last - i - 1
                    break
            for i in range(last+1, len(Q)):
                if Q[i] == 1:
                    R =  i - last - 1
                    break
            Max = max(L,R)
            Min = min(L,R)
            break
        point = (0, 0)
        maxPoint = 0
        L = 0
        S = 0
        for i in range(1, len(Q)):
            if Q[i] == 1:
                S = i
                maxbetween = S - L
                if maxbetween > maxPoint:
                    point = (L,S)
                    maxPoint = maxbetween
                L = S
        LN, SN = point 
        index = LN + int((SN-LN)/2)
        Q[index] = 1
        last = index
        K =  K - 1
    return Max, Min

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    T = int(f.readline())
    for case in range(1,T+1):
        N, K = [int(x) for x in f.readline().split()]
        maxAnswer, minAnswer = solve(N, K)
        print("Case #{0}: {1} {2}".format(case, maxAnswer, minAnswer))