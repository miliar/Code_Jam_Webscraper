fin = open('in', 'r')
fout = open('out', 'w')

num_of_cases = int(fin.readline())
base_cookie_rate = 2.0

def should_buy_factory(cookie_rate, factory_cost, factory_rate, goal_score):
    time_with_factory = (goal_score / (cookie_rate + factory_rate))
    time_without_factory = ((goal_score - factory_cost) / cookie_rate)
    return time_with_factory < time_without_factory

def calculate_optimal_time(factory_cost, factory_rate, goal_score):
    cookie_rate = base_cookie_rate
    time = 0.0
    have_enough_cookies = False
    if goal_score <= factory_cost:
        return goal_score / base_cookie_rate
    while not have_enough_cookies:
        if should_buy_factory(cookie_rate, factory_cost, factory_rate, goal_score):
            time += factory_cost / cookie_rate
            cookie_rate += factory_rate
        else:
            time += goal_score / cookie_rate
            have_enough_cookies = True
    return time

for i in range(num_of_cases):
    factory_cost, factory_rate, goal_score = [float(param) for param in fin.readline().split()]
    fout.write('Case #' + str(i + 1) + ': ' + str(calculate_optimal_time(factory_cost,
                                                                         factory_rate,
                                                                         goal_score)) + '\n')

fin.close()
fout.close()
