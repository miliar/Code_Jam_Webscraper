def solve (dist, horses, current, dest, time, horse_speed, horse_distance_left):
    if horse_distance_left < 0:
        return -1

    if current == dest:
        return time

    distance = dist[current][current+1]

    if current == 0:
        # Starting point
        speed = horses[current][1]
        return solve (dist, horses, current + 1, dest, time + distance/speed, speed, horse_distance_left - distance)
    else:
        # in the middle of nowhere
        same_horse_time = solve (dist, horses, current + 1, dest, time + distance/horse_speed, horse_speed, horse_distance_left - distance)

        new_horse_distance = horses[current][0]
        new_speed = horses[current][1]
        switch_horse_time = solve(dist, horses, current + 1, dest, time + distance/new_speed, new_speed, new_horse_distance - distance)

        if same_horse_time == -1:
            return switch_horse_time
        if switch_horse_time == -1:
            return same_horse_time
        if same_horse_time > switch_horse_time:
            return switch_horse_time
        else:
            return same_horse_time

rows = int(input())
for i in range(rows):
    N, Q = input().split(' ')
    N = int(N)
    Q = int(Q)

    horses = []
    for c in range(N): 
        d, s = input().split()
        horses.append( ( int(d), int(s)) )

    dist = []
    for d in range(N):
        get_input = input().split()
        for t in range(len(get_input)):
            get_input[t] = int(get_input[t])
        dist.append(get_input)
    start, stop = input().split()

    print('Case #' + str(i+1) + ': ' + str(solve(dist, horses, int(start)-1, int(stop)-1, 0, horses[0][1], horses[0][0])))
