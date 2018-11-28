from itertools import product


def solve():
    A, B, K = [int(i) for i in raw_input().split(' ')]
#    print A, B, K
    wins = 0
    for a, b in product(xrange(A), xrange(B)):
        if a & b < K:
            wins += 1
    return wins


if __name__ == "__main__":
    T = int(raw_input())
    for t in range(1, T + 1):
        out = solve()
        print "Case #{}: {}".format(t, out)
