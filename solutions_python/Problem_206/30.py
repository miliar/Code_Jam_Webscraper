from sys import stdin

def solve(t):
    line = stdin.readline().split(' ')
    d = int(line[0])
    n = int(line[1])

    max_time = 0

    for i in range(0, n):
        line = stdin.readline().split(' ')
        s = float(line[0])
        k = float(line[1])
        ti = (d - s) / k
        max_time = max(max_time, ti)

    res = d / max_time

    print('Case #' + str(t + 1) + ': ' + str(res))

T = int(stdin.readline())
for t in range(0, T):
    solve(t)
