T = int(input())

for t in range(T):
    _S, _K = input().split()
    K = int(_K)

    S = [x == "+" for x in _S]

    moves = 0
    for i in range(len(S) - K + 1):
        if not S[i]:
            moves += 1
            for j in range(K):
                S[i+j] ^= True
    if all(S):
        print("Case #{}: {}".format(t+1, moves))
    else:
        print("Case #{}: IMPOSSIBLE".format(t+1))
