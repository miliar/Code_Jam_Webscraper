def solve(T, S, K):
    flips = 0
    S = [x == '+' for x in S]
    for i in range(0, len(S) - K + 1):
        if not S[i]:
            flips += 1
            for j in range(i, i+K):
                S[j] = not S[j]
    if all(S):
        print("Case #{}: {}".format(T, flips))
    else:
        print("Case #{}: {}".format(T, "IMPOSSIBLE"))


if __name__ == '__main__':
    T = int(input())
    for i in range(1, T + 1):
        line = input().split()
        S, K = line[0], int(line[1])
        solve(i, S, K)
