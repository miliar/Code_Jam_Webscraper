import fileinput

def give_me_min_time(farm_cost, increase, expected):
    if expected < farm_cost:
        return expected / 2.0

    tries = int(expected / farm_cost)

    accum = 0
    current_speed = 2.0
    min_time = expected / 2.0 + 1
    while(True):
        if accum + (float(expected) / current_speed) < min_time:
            min_time = accum + float(expected) / current_speed
            accum += float(farm_cost) / current_speed
            current_speed += increase

        else:
            break
    return min_time
        


def main():
    num_cases = int(raw_input())
    for i in xrange(num_cases):
        farm_cost, increase, expected = map(float, raw_input().split(' '))
        
        t = give_me_min_time(farm_cost, increase, expected)
        
        print 'Case #%s: %0.6f' % ((i+1), t)
        

if __name__ == '__main__':
    main()
