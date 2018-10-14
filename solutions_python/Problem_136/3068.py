T = int(input())

for i in range(1, T+1):
    z = input().split(' ')
    C = float(z[0]) #cost of farm
    F = float(z[1]) #farm cps
    X = float(z[2]) #goal cookies
    time = 0.0
    cps = 2.0

    while(True):
        time_to_goal_1 = X/cps
        time_to_farm = C/cps
        cps += F
        time_to_goal_2 = X/cps

        if time_to_goal_1 < time_to_goal_2 + time_to_farm:
            time += time_to_goal_1
            break
        else:
            time += time_to_farm

    print("Case #%d: %.7f" % (i,time))