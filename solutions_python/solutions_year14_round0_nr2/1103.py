input = open("input.txt", "r")

cases = int(input.readline())

for case in range(cases):
    cookies_per_sec = 2.0
    this_game = map(float, input.readline().split())
    farm_cost = this_game[0]
    farm_boost = this_game[1]
    win_total = this_game[2]
    
    current_cookies = 0.0
    
    if win_total < farm_cost:
        #print win_total, farm_cost
        win_time = (1 / cookies_per_sec) * win_total
        #print "Here"
    else:
        win_time = 0
        while True:
            time_to_farm = (farm_cost / cookies_per_sec)
            time_with_farm = ((1 / (cookies_per_sec + farm_boost)) * win_total) + time_to_farm
            time_to_win = (1 / cookies_per_sec) * win_total
            #print time_to_win, time_with_farm, time_to_farm
            if time_to_win < time_with_farm:
                win_time += time_to_win
                break
            else:
                win_time += time_to_farm
                cookies_per_sec += farm_boost

    
    print "Case #%i: %.7f" % (case+1, win_time)

input.close()

#Time until first buy
#Check if faster to buy again or wait