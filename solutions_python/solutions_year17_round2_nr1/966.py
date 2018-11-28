from Carbon.Sound import timbreCmd
def solve(line):
    d, n = map(int, line.split())
    h = [(0, 0) for i in range(n)]
    for i in range(n):
        h[i] = tuple(map(int, sys.stdin.readline().rstrip().split()))
    tmax = max([(d - i[0]) * 1.0 / i[1] for i in h])
    return d/tmax
