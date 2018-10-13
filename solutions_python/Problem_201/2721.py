def solve(T, N, K):
    stalls = [True] + [False] * N + [True]
    for person in range(K):
        best_idx = 0
        best_mi = 0
        best_ma = 0
        for j in range(1, N+1):
            if stalls[j]:
                continue
            Ls = 0
            for k in range(j-1, 0, -1):
                if stalls[k]:
                    break
                Ls += 1
            Rs = 0
            for k in range(j+1, N+2):
                if stalls[k]:
                    break
                Rs += 1
            mi = min(Ls, Rs)
            ma = max(Ls, Rs)
            if mi > best_mi:
                best_mi, best_ma = mi, ma
                best_idx = j
            elif mi == best_mi and ma > best_ma:
                best_mi, best_ma = mi, ma
                best_idx = j
        stalls[best_idx] = True
    print("Case #{}: {} {}".format(T, best_ma, best_mi))

if __name__ == '__main__':
    T = int(input())
    for i in range(1, T + 1):
        line = input().split()
        N, K = int(line[0]), int(line[1])
        solve(i, N, K)
