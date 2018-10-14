from sys import stdin

for i in range(int(stdin.readline())):
    case = i + 1
    (farm_cost, farm_cookies, target) = map(float, stdin.readline().split())

    time = 0
    speed = 2
    while True:
        farm_time = farm_cost / speed
        target_time = target / speed
        next_target_time = farm_time + (target / (speed + farm_cookies))
        if target_time <= farm_time or target_time <= next_target_time:
            time += target_time
            break
        else:
            time += farm_time
            speed += farm_cookies

    print "Case #{:}: {:}".format(case, time)
