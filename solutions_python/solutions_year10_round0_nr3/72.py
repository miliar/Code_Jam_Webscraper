import sys

def read():
    return sys.stdin.readline().split(" ")

def solve_case():
    R, k, N = map(int, read())
    g = map(int, read())

    length, am = [0] * N, [0] * N
    for i in range(N):
        while length[i] < N and am[i] + g[(i + length[i]) % N] <= k:
            am[i] += g[(i + length[i]) % N]
            length[i] += 1

        if i + 1 < N:
            length[i + 1] = length[i] - 1
            am[i + 1] = am[i] - g[i]

    seen = {}
    ride, pos, ans = 0, 0, 0
    while ride < R:
        if pos in seen:
            ans_delta = ans - seen[pos][0]
            ride_delta = ride - seen[pos][1]

            times = (R - ride) / ride_delta
            ans += times * ans_delta
            ride += times * ride_delta

        if ride < R:
            seen[pos] = (ans, ride)

            ans += am[pos]
            pos = (pos + length[pos]) % N
            ride += 1

    print ans

def main():
    test_cases, = map(int, read())
    for case in range(1, test_cases + 1):
        print ("Case #%d:" % case),
        solve_case()

if __name__ == "__main__":
    main()


