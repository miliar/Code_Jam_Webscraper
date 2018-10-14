import sys
T = int(sys.stdin.readline())


def main():
    for case in range(1, T + 1):
        res = solve(case)
        sys.stdout.write("Case #{}: {}\n".format(case, res))


def solve(case):
    inp = sys.stdin.readline().split()
    s_max = int(inp[0])
    ks = map(int, list(inp[1]))

    up = 0
    missing = 0

    for si in range(0, s_max + 1):
        ki = ks[si]

        if up < si:
            missing += si - up
            up += si - up

        up += ki

    return missing


main()
