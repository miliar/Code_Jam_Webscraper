def solve(D, Ks, Ss):
    max_T = max((D - K)/S for K, S in zip(Ks, Ss))
    return D/max_T


T = int(input())

for i in range(T):
    D, N = [int(x) for x in input().split(' ')]
    Ks = []
    Ss = []
    for j in range(N):
        K, S = [int(x) for x in input().split(' ')]
        Ks.append(K)
        Ss.append(S)

    print('Case #{}: {}'.format(i + 1, solve(D, Ks, Ss)))
