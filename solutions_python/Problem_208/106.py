import sys

def solve(distances, horses):
    a = [999999999999999 for _ in range(len(horses))]
    last_horse_speed, last_horse_dist = horses[len(horses)-2]
    a[len(a)-1] = 0
    a[len(a)-2] = distances[-1] / last_horse_speed if last_horse_dist >= distances[-1] else 99999999999999

    for i in range(len(a)-3, -1, -1):
        this_horse_speed, this_horse_dist = horses[i]
        total_dist = 0
        best_time = 9999999999999
        for j in range(i+1, len(a)):
            total_dist += distances[j-1]
            if total_dist > this_horse_dist:
                break
            time = a[j] + total_dist / this_horse_speed
            if time < best_time:
                best_time = time
        a[i] = best_time
    return a[0]

t = int(next(sys.stdin))
for test in range(t):
    n, q = [int(s) for s in next(sys.stdin).strip().split(' ')]
    assert q == 1
    horses = []
    for _ in range(n):
        horses.append(tuple(reversed([float(s) for s in next(sys.stdin).strip().split(' ')])))
    distances = []
    for i in range(n):
        j = i+1
        arr = [float(s) for s in next(sys.stdin).strip().split(' ')]
        if j >= n:
            break
        distances.append(arr[j])
    next(sys.stdin)
    print('Case #{}: {}'.format(test+1, solve(distances, horses)))
