from codejam import readfile, takeby
import sys

sys.setrecursionlimit(100000)

problems = readfile()[1:]

BASE_RATE = 2.

def find_maximum_farm(farm_cost, farm_bonus, win_count, current_rate, total_time):
    new_win_cost = (win_count/(current_rate + farm_bonus)) + farm_cost/current_rate
    if (win_count/current_rate < new_win_cost):
        return total_time + win_count/current_rate
    else:
        return find_maximum_farm(farm_cost, farm_bonus, win_count, 
            current_rate+farm_bonus, total_time + farm_cost/current_rate)

for index, problem in enumerate(problems, 1):
    print "Case #%s:" % index,
    farm_cost, farm_bonus, win_count = map(float, problem.split())

    if farm_cost == 0:
        print 0
        continue
    answer = find_maximum_farm(farm_cost, farm_bonus, win_count, BASE_RATE, 0.0)
    print answer
