with open('B-small-attempt0.in', 'r') as f:
    num_test_cases = int(f.readline())

    for test_case in range(num_test_cases):
        params = [float(string) for string in f.readline().split()]

        farm_cost = params[0]
        farm_prod_rate = params[1]
        target = params[2]
        starting_prod_rate = 2

        found_optimal_time = False

        num_farms = 0
        optimal_time = float('inf')

        while not found_optimal_time:
            current_prod_rate = 2

            new_time = 0

            for i in range(num_farms):
                new_time += farm_cost / (starting_prod_rate + farm_prod_rate * i)

            new_time += target / (starting_prod_rate + farm_prod_rate * num_farms)

            if new_time > optimal_time:
                found_optimal_time = True
            else:
                optimal_time = new_time

            num_farms += 1

        print "Case #" + str(test_case + 1) + ": " + "%.7f" % optimal_time