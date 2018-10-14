import csv
import sys


def decide(goal, rate, farm_cost, farm_output):
    time_to_goal = goal / rate
    time_to_goal_with_farm = (farm_cost / rate) + (goal / (rate + farm_output))
    
    if time_to_goal < time_to_goal_with_farm:
        return True, time_to_goal
    else:
        return False, time_to_goal_with_farm


infile = csv.reader(open(sys.argv[1], 'r'), delimiter=' ')

cases = int(infile.next()[0])

for case in xrange(cases):
    rate = 2.0

    farm_cost, farm_output, goal = map(float, infile.next())

    farm_time_offset = 0
    
    terminate, time_to_goal = decide(goal, rate, farm_cost, farm_output)
    
    while not(terminate):
        farm_time_offset += farm_cost / rate
        rate += farm_output
        terminate, time_to_goal = decide(goal, rate, farm_cost, farm_output)
    
    print "Case #%u: %.7f" % (case + 1, time_to_goal + farm_time_offset)
    