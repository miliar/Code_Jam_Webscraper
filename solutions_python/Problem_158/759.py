import sys


def solve(instream):
    line = instream.readline().strip()
    x, r, c = [int(x) for x in line.strip().split(" ") if x]
    if x >= 7:
        return "RICHARD"

    if x > r and x > c:
        return "RICHARD"

    if x > r + c - 1:
        return "RICHARD"

    if x > min(r, c) * 2:
        return "RICHARD"

    if x == 4 and min(r, c) == 2:
        return "RICHARD"

    if x == 6 and min(r, c) <= 4:
        return "RICHARD"

    return "GABRIEL" if ((r * c) % x == 0) else "RICHARD"


def run(input=sys.stdin):
    cases = int(input.readline().strip())
    for i in range(cases):
        print("Case #{}: {}".format(i + 1, solve(input)))

if __name__ == "__main__":
    run()
