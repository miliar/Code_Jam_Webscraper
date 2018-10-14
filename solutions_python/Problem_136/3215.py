from operator import add
num_test_cases = int(raw_input())



def solve(cost_farm, farm_output, limit):
    time = [0.0]
    produce = []
    prod_rate = 2.0

    # seconds after which you can buy a farm
    while (True):
        cost_to_farm = cost_farm / prod_rate
        cost_to_limit = limit / prod_rate

        hyp_cost_to_limit = limit / (prod_rate + farm_output)

        hyp_cost = (hyp_cost_to_limit + cost_to_farm)

        current_cost = cost_to_limit

        if hyp_cost < current_cost:
            prod_rate = prod_rate + farm_output
            time.append(cost_to_farm)
        else:
            time.append(current_cost)
            return reduce(add,time)










for j in xrange(1, num_test_cases + 1):

    c,f,x = [float(x) for x in (raw_input().split())]
    print "Case #" + str(j) + ": " + "%.7f" % solve(c,f,x)
