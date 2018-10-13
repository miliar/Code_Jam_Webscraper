file_name = 'B-large.in'

def get_shortest_game_time(farm_cost, farm_cookies_ps, goal):

    cur_time = 0.0
    cookies_ps = 2.0

    time_left = cur_time + (goal / cookies_ps)
    #                                   time to build farm   +  time to goal with faster c/ps
    time_left_with_farm = cur_time + (farm_cost / cookies_ps) + ((goal) / (cookies_ps+farm_cookies_ps))


    while time_left > time_left_with_farm:
        #build farm
        cur_time += farm_cost / cookies_ps
        cookies_ps += farm_cookies_ps

        #re calculate
        time_left = cur_time + (goal / cookies_ps)
        time_left_with_farm = cur_time + (farm_cost / cookies_ps) + ((goal) / (cookies_ps+farm_cookies_ps))

    time_taken = time_left
    return time_taken




with open(file_name, 'r') as infile:
    cases = int(infile.readline())
    for case in range(1, cases+1):
        farm_cost, farm_cookies, goal = [float(x) for x in infile.readline().split(' ')]
        shortest_time = get_shortest_game_time(farm_cost, farm_cookies, goal)
        print 'Case #%d: %.7f' % (case, shortest_time)



