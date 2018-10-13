import fileinput


def solve(time_array, source, target):
    N = len(time_array)
    real_time = []
    max_time = time_array[source][target]
    for n in range(N):
        real_time.append([max_time] * N)
        real_time[-1][n] = 0

    queue = [source]
    while len(queue) > 0:
        s = queue.pop(0)
        for t in range(N):
            if real_time[source][s] + time_array[s][t] > max_time:
                continue
            if real_time[source][s] + time_array[s][t] < real_time[source][t]:
                real_time[source][t] = real_time[source][s] + time_array[s][t]
                if target == t:
                    max_time = real_time[source][t]
                else:
                    queue.append(t)

    return real_time[source][target]




def make_time_arr(horses, distance):
    N = len(horses)
    time_dist = []
    max_time = 10**12
    for n in range(N):
        time_dist.append([max_time] * N)
        time_dist[-1][n] = 0

    for i, h in enumerate(horses):
        hdist, hspeed = h
        queue = [(i, hdist)]

        while len(queue) > 0:
            source, dist = queue.pop(0)
            for target in range(N):
                if distance[source][target] < 0 or distance[source][target] > dist:
                    continue
                time = distance[source][target] / hspeed
                if time_dist[i][source] + time < time_dist[i][target]:
                    time_dist[i][target] = time_dist[i][source] + time
                    queue.append((target, dist - distance[source][target]))

    return time_dist

inp = fileinput.input()

num_cases = int(inp.readline())
for t in range(1, num_cases + 1):
    N, Q = (int(x) for x in inp.readline().split())
    horses = []
    for _ in range(N):
        horses.append(tuple(int(x) for x in inp.readline().split()))
    distance = []

    for _ in range(N):
        distance.append(tuple(int(x) for x in inp.readline().split()))
        assert len(distance[-1]) == N

    time_arr = make_time_arr(horses, distance)

    times = []
    for _ in range(Q):
        U,V = (int(x) for x in inp.readline().split())
        times.append(solve(time_arr, U-1, V-1))

    print("Case #{}: {}".format(t, " ".join("{:.6f}".format(t) for t in times)))