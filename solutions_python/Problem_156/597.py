def solve(P):
    counts = [0] * (max(P) + 1)
    for p in P:
        counts[p] += 1

    best = len(counts)
    for i in range(1, len(counts)):
        time = i
        for j in range(i + 1, len(counts)):
            moves = j / i
            if j % i == 0:
                moves -= 1
            time += counts[j] * moves
        if time < best:
            best = time
    return best

T = int(raw_input())
for i in range(T):
    D = int(raw_input())
    P = map(int, raw_input().split())
    ans = solve(P)
    print "Case #{}: {}".format(i + 1, ans)
