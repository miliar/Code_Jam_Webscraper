T = input()

for t in range(T):

    C,F,X = [float(f) for f in raw_input().split(' ')]
    p_rate = 2
    n_farms = 0
    result = 0.0

    wait_cost = (X) / ( p_rate + (n_farms * F) )
    farm_cost = (C) /  ( p_rate + (n_farms * F) )
    wait_cost_after_farm = (X) / ( p_rate   + ((n_farms+1) * F) )

    while (wait_cost > farm_cost + wait_cost_after_farm):

        result += farm_cost
        n_farms += 1

        wait_cost = (X) / ( p_rate + (n_farms * F) )
        farm_cost = (C) /  ( p_rate + (n_farms * F) )
        wait_cost_after_farm = (X) / ( p_rate   + ((n_farms+1) * F) )
        # print wait_cost,farm_cost,wait_cost_after_farm

    result += wait_cost


    print "Case #" + str(t+1) + ": " + str(result)

