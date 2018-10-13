def should_buy(current_cookies, current_speed, farm_cost, farm_bonus, objective):
    # For each farm, we compute if it's faster to get to objective by buying the farm or not
    time_buy = time_required(current_cookies - farm_cost, current_speed + farm_bonus, objective)
    time_keep = time_required(current_cookies, current_speed, objective)
    return time_buy < time_keep

def time_required(current_cookies, current_speed, objective):
    remaining = objective - current_cookies
    return remaining / current_speed


def solution(farm_cost, farm_bonus, objective):
    current_cookies = 0
    current_speed = 2
    current_time = 0
    while(current_cookies < objective):
        if objective < farm_cost:
            # Getting to the objective is faster than getting to buy a farm
            return current_time + time_required(current_cookies, current_speed, objective)
        else:
            # Fast forward to when we are able to buy a farm
            current_time += time_required(current_cookies, current_speed, farm_cost)
            current_cookies = farm_cost
            
            # decide if we should buy a farm
            if should_buy(current_cookies, current_speed, farm_cost, farm_bonus, objective):
                # we have bough a farm
                current_cookies = 0
                current_speed += farm_bonus
            else:
                # we will keep our cookies till the end
                return current_time + time_required(current_cookies, current_speed, objective)



if __name__ == '__main__':
    with open('test.txt') as in_stream:
        with open('result.txt', 'w') as out_stream:
            t = int(in_stream.readline())
            for i in xrange(t):
                c, f, x = map(float, in_stream.readline().split(' '))
                result = solution(c, f, x)
                out_stream.write("Case #{}: {:0.7f}\n".format(i+1, result))

    # import random
    # with open('test.txt', 'w') as stream:
    #     stream.write('100\n')
    #     for t in xrange(100):
    #         c = random.uniform(1, 500)
    #         f = random.uniform(1, 4)
    #         x = random.uniform(1, 2000)
    #         stream.write('{} {} {}\n'.format(c, f, x))
