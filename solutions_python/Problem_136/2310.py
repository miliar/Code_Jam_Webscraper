import sys
lines = [line for line in sys.stdin]
test_cases = int(lines[0])

for test in xrange(test_cases):
    stuff = [float(f) for f in lines[test + 1].split(' ')]
    
    cost_of_farm = stuff[0]
    increase_from_farm = stuff[1]
    goal = stuff[2]

    time = 0
    farms = 0
    while True:
        time_till_next_farm = cost_of_farm / (2 + increase_from_farm * farms) 
        time_till_goal = goal /  (2 + increase_from_farm * farms)
        time_till_goal_with_farm = goal /  (2 + increase_from_farm * (farms + 1) )

        if time_till_next_farm + time_till_goal_with_farm < time_till_goal:
            time += time_till_next_farm
            farms += 1
        else:
            time += time_till_goal
            break

    print "Case #%d: %f" % (test+1, time)





