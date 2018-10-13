import sys
T = int(sys.stdin.readline())


def main():
    for case in range(1, T + 1):
        res = solve(case)
        sys.stdout.write("Case #{}: {}\n".format(case, res))


def solve(case):
    inp = sys.stdin.readline().split()
    x = int(inp[0])
    r = int(inp[1])
    c = int(inp[2])

    if r < x and c < x:
        return "RICHARD"

    if x % 2 == 0:
        if r < x / 2 or c < x / 2:
            return "RICHARD"

    else:
        if r < (x + 1) / 2 or c < (x + 1) / 2:
            return "RICHARD"

    if r * c % x == 0:
        if r * c == 8 and x == 4:
            return "RICHARD"
        else:
            return "GABRIEL"
    else:
        return "RICHARD"


main()
