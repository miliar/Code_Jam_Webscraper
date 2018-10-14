def solve(d, lines):
    tmax = -1
    for k, s in lines:
        t = 1.0 * (d-k) / s
        tmax = max(t, tmax)
    return d / tmax


def main():
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        d, n = [int(c) for c in raw_input().split(" ")]
        lines = []
        for j in xrange(0, n):
            lines.append([int(c) for c in raw_input().split(" ")])
        sol = solve(d, lines)
        print "Case #{}: {:.6f}".format(i, sol)


if __name__ == "__main__":
    main()
