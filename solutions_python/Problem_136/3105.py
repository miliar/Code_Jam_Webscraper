from pprint import pprint

def compute_time(rate, goal):
    return float(goal) / float(rate)

for case in xrange(input()):
    farm_cost, farm_rate, goal = map(float, raw_input().split())
    current_farms = 0
    current_time = compute_time(2, goal)
    running_total_farming_time = 0

    time_to_get_next_farm = compute_time(2 + current_farms*farm_rate, farm_cost)
    running_total_farming_time += time_to_get_next_farm
    current_farms += 1
    time_to_get_goal = compute_time(2 + current_farms*farm_rate, goal)
    next_time = time_to_get_goal + running_total_farming_time

    while current_time >= next_time:
        current_time = next_time
        time_to_get_next_farm = compute_time(2 + current_farms*farm_rate, farm_cost)
        running_total_farming_time += time_to_get_next_farm
        current_farms += 1
        time_to_get_goal = compute_time(2 + current_farms*farm_rate, goal)
        next_time = time_to_get_goal + running_total_farming_time

    print 'Case #{0}: {1:.7f}'.format(case + 1, current_time)
