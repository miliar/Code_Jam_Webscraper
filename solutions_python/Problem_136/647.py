with open("B-large.in") as f:
    for case in xrange(int(f.readline())):
        cookies_per_second = 2.0
        cost_per_farm, additional_per_second, goal = [float(num) for num in f.readline().split(" ")]
        if goal < cost_per_farm:
            print "Case #%d: %.7f" % (case+1, goal/cookies_per_second)
            continue

        best_so_far = goal/cookies_per_second
        time_to_buy_i_farms = cost_per_farm/cookies_per_second
        for i in xrange(1, 100000000):
            current_rate = 2.0 + (i * additional_per_second)
            time_to_goal = time_to_buy_i_farms + (goal/current_rate)
            time_to_buy_i_farms += cost_per_farm/current_rate

            if time_to_goal < best_so_far:
                best_so_far = time_to_goal
            else:
                print "Case #%d: %.7f" % (case+1, best_so_far)
                break


"""
4
30.0 1.0 2.0
30.0 2.0 100.0
30.50000 3.14159 1999.19990
500.0 4.0 2000.0


Case #1: 1.0000000
Case #2: 39.1666667
Case #3: 63.9680013
Case #4: 526.1904762

"""
