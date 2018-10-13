T = int(input())

for i in range(1, T+1):
    time = 0
    crate = 2.0
    cost, frate, goal = list(map(float, input().split())) # factory cost, factory cookie rate, goal

    while(1):
        tfinal = goal / crate
        tneeded = cost / crate
        trec = tneeded + (goal / (crate+frate))

        if (trec < tfinal):
            time += tneeded
            crate += frate
        else:
            time += tfinal
            break

    print ('Case #%s: %.7f' % (i, time))

