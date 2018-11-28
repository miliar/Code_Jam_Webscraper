def run_sim_new(farm_cost, farm_rate, goal):
    cookie_rate = 2.0
    farm_time = 0.0
    time_elapsed = 0.0
    while(True):
        finish_cur = farm_time + goal / cookie_rate
        farm_time  += farm_cost / cookie_rate
        finish_new = farm_time + (goal / (cookie_rate + farm_rate)) 
        if(finish_cur < finish_new):
            time_elapsed = finish_cur
            break
        else:
            cookie_rate += farm_rate
    return time_elapsed

num_tests = int(input())
for i in range(num_tests):
    farm_cost, farm_rate, goal = [float(i) for i in input().split()]
    #print(str(farm_cost) + " " + str(farm_rate) + " " + str(goal))
    time_elapsed= run_sim_new(farm_cost, farm_rate, goal)
    print("Case #" + str(i + 1) + ": " + ("{0:.7f}".format(time_elapsed)))
