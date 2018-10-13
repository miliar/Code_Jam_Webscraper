num_tests = int(raw_input())

for t in range(num_tests):
    case = t + 1

    rate = 2
    
    input = raw_input().split(' ')
    farm_price = float(input[0])
    cookies_per_sec = float(input[1])
    goal = float(input[2])

    fastest_time = goal/rate

    not_found = True
    total_cookies = 0
    time_spent_buying_farms = 0
    time_per_farm = farm_price/rate
    
    while(not_found):
        
        time_spent_buying_farms += time_per_farm
        rate += cookies_per_sec
        time_per_farm = farm_price/rate
        new_time = (goal/rate) + time_spent_buying_farms
            
        if (new_time < fastest_time):
                fastest_time = new_time
        else:
                not_found = False

    print 'Case #' + str(case) + ': ' + str(fastest_time)



