cases = int(raw_input())

for case in range(1, cases+1):
    c, f, x = [float(i) for i in raw_input().split(' ')]

    rate = 2
    time = 0

    while True:
        time_to_farm = c / rate # 250
        time_to_complete = x / rate # 1000

        time_to_complete_with_next_farm = x / (rate + f)

        if time_to_complete <= (time_to_farm + time_to_complete_with_next_farm):
            time += time_to_complete
            break
        else:
            time += time_to_farm
            rate += f

    print "Case #{0}: {1:.8f}".format(case, time)
