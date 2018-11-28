from __future__ import division

try: input = raw_input
except NameError: pass

for t in range(1, int(input()) + 1):
    farm_cost, added_rate, target = [float(i) for i in input().split()]
    production = 2.0
    time_so_far = 0.0
    while 1:
        time_to_buy_farm = farm_cost/production
        time_to_target = target/production
        if time_to_target > time_to_buy_farm + target/(production+added_rate):
            time_so_far += time_to_buy_farm
            production += added_rate
        else:
            time_so_far += time_to_target
            break
    fmt_str = 'Case #' + str(t) + ': {:.7f}'
    print fmt_str.format(time_so_far)
