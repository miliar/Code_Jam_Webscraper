def calc_rate(r, c, f, x):
    total_time = 0
    while True:
        current_rate = x / r
        current_rate_plus = x / (r+f)
        next_farm = c / r

        if current_rate - current_rate_plus > next_farm:
            total_time += next_farm
            r += f
        else:
            total_time += current_rate
            break

    return total_time

for case in range(int(raw_input())):
    c, f, x = map(float, raw_input().split())
    print "Case #%d: %s" % (case+1, calc_rate(2.0, c, f, x))
