import sys


def calc(dp, start, end, work):
    if dp[start][end][work] >= 0.0:
        return dp[start][end][work]

    mid = (start + end) // 2
    rv = 0.0

    for i in range(0, work + 1):
        left_work = i
        right_work = work - i

        prob_left = calc(dp, start, mid, left_work)
        prob_right = calc(dp, mid + 1, end, right_work)
        rv += prob_left * prob_right

    dp[start][end][work] = rv

    return rv


def solve(N, K, U, P):
    # TODO Solve the problem
    P.sort()

    while U > 0.0:
        base = P[N - K]
        cnt_min = 1
        i = N

        for i in range(N - K + 1, N):
            if P[i] == base:
                cnt_min += 1
            else:
                break

            if i == N - 1:
                i += 1

        nxt = i

        if nxt == N:
            target = 1.0
        else:
            target = P[nxt]

        needed = (target - base) * cnt_min

        if needed > 0.0:
            if U > needed or abs(U - needed) < 1e-6:
                for i in range(N - K, nxt):
                    P[i] = target

                U -= needed
            else:
                for i in range(N - K, nxt):
                    P[i] += U / cnt_min

                U = 0.0
        else:
            break

    if U > 0.0:
        for i in reversed(range(0, N - K)):
            needed = 1 - P[i]

            if U >= needed:
                P[i] = 1.0
                U -= needed
            else:
                P[i] += U
                U = 0.0
                break

    dp = [[[-1.0 for _ in range(N + 1)] for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                dp[i][j][0] = 1 - P[i]
                dp[i][j][1] = P[i]

                for k in range(2, N + 1):
                    dp[i][j][k] = 0.0

    rv = 0.0

    for i in range(K, N + 1):
        rv += calc(dp, 0, N - 1, i)

    return rv


""" Convert the input file into a list of strings """
in_file = sys.argv[1]

with open(in_file, "r") as f:
    data = f.read()

lines = data.splitlines()
""" Convert the input file into a list of strings """

""" Interpret the arguments """
cases = int(lines.pop(0))

for i in range(1, cases + 1):
    line = lines.pop(0)
    N, K = line.split()
    N, K = int(N), int(K)

    U = float(lines.pop(0))

    P = lines.pop(0).split()
    P = [float(x) for x in P]

    answer = solve(N, K, U, P)

    print('Case #{0}: {1}'.format(i, answer))
""" Interpret the arguments """
