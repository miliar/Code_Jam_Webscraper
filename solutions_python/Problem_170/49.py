"""Solve the '2C' problem (GCJ 2015)."""

from solver import solver


def solve(s, e, f, c=float('inf')):
    if not s:
        return len(e & f)
    return min(solve(s[1:], e.union(s[0]), f),
               solve(s[1:], e, f.union(s[0])))


@solver(lines_per_case="dynamic")
def gcj_2c(lines):
    s = [line.strip().split() for line in lines]
    e, f = set(s[0]), set(s[1])
    return solve(s[2:], e, f)


if __name__ == "__main__":
    gcj_2c.from_cli()
