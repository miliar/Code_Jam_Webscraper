def solve(N, K, U, P):
    P_s = sorted(P)
    Us = U
    if N != K:
        return 0

    for i in range(N):
        if i < N - 1 and Us >= (i+1) * (P_s[i+1] - P_s[i]):
            Us = Us - (P_s[i+1] - P_s[i]) * (i + 1.)
        else:
            t = Us / (i + 1.)
            prob = (P_s[i] + t) ** (i + 1.)
            for j in range(i+1, N):
                prob = P_s[j] * prob
            return prob


def main():

    import sys
    with open(sys.argv[1]) as f:
        nums = int(f.readline())

        for i in range(nums):
            N,K = f.readline().strip().split()
            N = int(N)
            K = int(K)
            U = float(f.readline())
            P = [float(p) for p in f.readline().split(' ')]
            ans = solve(N, K, U, P)
            print("Case #{}: {}".format(i+1, ans))


if __name__ == "__main__":
    main()
