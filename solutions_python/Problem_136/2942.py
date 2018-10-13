#!/USSR/bin/env python3

num_cases = int(input())

for i in range(num_cases):
    # cost of farm, farm bonus, cookies to win
    C, F, X = [float(x) for x in input().split()]

    rate = 2
    next_strat = 0
    best_time = X / rate

    while True:
        # print("Rate:", rate)
        # print("Time:", next_strat)
        # print("Best:", best_time)
        farm_in = C / rate
        next_strat += farm_in
        rate += F
        # print("Time to farm:", farm_in)
        # print("Time to win:", X / rate)
        # print("New strat:", next_strat)
        if (next_strat + (X / rate)) < best_time:
            best_time = next_strat + (X / rate)
        else:
            break
    print("Case #{}: {}".format(i + 1, best_time))
