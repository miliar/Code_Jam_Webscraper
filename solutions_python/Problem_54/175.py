from gcd import gcd
import sys

def diff(v):
    return [(v[i+1] - v[i]) for i in range(len(v) - 1)]

def calc_gcd(v):
    g = gcd(v[0], v[1])
    for i in v[2:]:
        g = gcd(g, i)
    return g

def solve(v):
    v.sort()
    diffs = diff(v)
    if len(diffs) == 1:
        diffs.append(diffs[0])
    g = calc_gcd(diffs)
    if v[0] % g == 0:
        return 0
    return g * ((v[0] / g) + 1) - v[0]

def main():
    ncases = int(sys.stdin.readline().strip())
    for i in range(ncases):
        values = [int(x) for x in sys.stdin.readline().strip().split()]
        print "Case #%d:" % (i+1), solve(values[1:])

if __name__ == "__main__":
    main()
