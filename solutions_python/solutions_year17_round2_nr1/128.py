import sys

def solve(d, starts, speeds):
    max_time = 0
    for start, speed in zip(starts, speeds):
        to_travel = d - start
        time = to_travel / speed
        if time > max_time:
            max_time = time
    return d / max_time

t = int(next(sys.stdin))
for test in range(t):
    d, n = [int(s) for s in next(sys.stdin).strip().split(' ')]
    speeds = []
    starts = []
    for i in range(n):
        start, speed = [float(s) for s in next(sys.stdin).strip().split(' ')]
        starts.append(start)
        speeds.append(speed)
    print('Case #{}: {}'.format(test+1, solve(d, starts, speeds)))
