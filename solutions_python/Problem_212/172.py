import sys
from datetime import datetime


def debug(x):
    sys.stderr.write('{} DEBUG: {}\n'.format(datetime.now().time(), x))


def solve():
    N, P = map(int, raw_input().split())
    bins = [0] * P
    gps = map(int, raw_input().split())
    for g in gps:
        bins[g%P] += 1
    debug(bins)
    ans = bins[0]
    rem = 0
    if P == 2:
        ans += bins[1]//2
        bins[1] = bins[1]%2

        ans += int(any(bins[1:]))

    elif P == 3:
        mn = min(bins[1], bins[2])
        bins[1] -= mn
        bins[2] -= mn
        ans += mn

        ans += bins[1]//3
        bins[1] = bins[1]%3

        ans += bins[2]//3
        bins[2] = bins[2]%3

        ans += int(any(bins[1:]))

    else:
        mn = min(bins[1], bins[3])
        bins[1] -= mn
        bins[3] -= mn
        ans += mn

        ans += bins[2]//2
        bins[2] = bins[2]%2

        mn = min(bins[2], bins[3]//2)
        bins[2] -= mn
        bins[3] -= 2*mn
        ans += mn

        mn = min(bins[2], bins[1]//2)
        bins[2] -= mn
        bins[1] -= 2*mn
        ans += mn

        ans += bins[1]//4
        bins[1] = bins[1] % 4

        ans += bins[3]//4
        bins[3] = bins[3] % 4

        ans += int(any(bins[1:]))

    return ans


def main():
    T = int(raw_input())
    for tc in xrange(1, T+1):
        debug("Running test #{}...\n".format(tc))
        print "Case #{}: {}".format(tc, solve())


if __name__ == "__main__":
    main()
