import sys

num_lines_per_case = 1
lines = sys.stdin.readlines()
num_cases = int(lines[0])

for i in xrange(1, num_cases + 1):
    (c, f, x) = tuple([float(t) for t in lines[i].split(' ')])
    num_farms = 0
    init_c_rate = 2
    cookie_making_time = 0
    prev_time = x / init_c_rate
    best_time = prev_time

    while True:
        cookie_making_time += c / (init_c_rate + num_farms * f)
        curr_time = cookie_making_time + x / (init_c_rate + (num_farms + 1) * f)

        if prev_time < curr_time:
            best_time = prev_time
            break

        prev_time = curr_time

        num_farms += 1

    print "Case #{}: {:.7f}".format(i, best_time)
