__author__ = 'tobias'

filename = 'B-large'
def rate_calc(farms):
    cur_rate = 2.0 + farm_rate * farms
    time_to_farm = farm_cost / cur_rate
    time_to_goal = target / cur_rate
    return time_to_farm, time_to_goal

with open('%s.in' % filename) as inp:
    with open('%s.out' % filename, 'w') as out:
        cases = inp.readline().strip()
        for case in range(int(cases)):
            farm_cost, farm_rate, target = inp.readline().strip().split()
            farm_cost, farm_rate, target = float(farm_cost), float(farm_rate), float(target)
            time = 0.0000
            for farms in range(1000000000000000000):
                time_to_farm, time_to_goal = rate_calc(farms)
                if (time_to_farm + rate_calc(farms + 1)[1]) > time_to_goal:
                    time += time_to_goal
                    break
                else:
                    time += time_to_farm
            output = time
            out.write("Case #{case}: {out:.7f}\n".format(case=case + 1, out=output))