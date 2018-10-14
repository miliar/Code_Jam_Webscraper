def time_formula(candies, factory_productivity, num_factories):
    return float(candies)/(2.0 + num_factories*factory_productivity)

def greedy(C, F, X):
    num_factories = 0
    time_spent = 0.0
    time_to_next_factory = time_formula(C, F, num_factories)
    while (time_formula(X, F, num_factories) + time_spent) > (time_formula(X, F, num_factories+1)+ time_to_next_factory + time_spent):
        time_spent += time_to_next_factory
        num_factories += 1
        time_to_next_factory = time_formula(C, F, num_factories)

    return time_spent + time_formula(X, F, num_factories)



def solver():
    num_test_cases = int(raw_input(""))
    for test_case_num in xrange(1, num_test_cases+1):
        C, F, X = map(float, raw_input("").split())
        time = greedy(C, F, X)
        print "Case #" + str(test_case_num) + ": " + format(time, ".7f")


if __name__ == '__main__':
    solver()
