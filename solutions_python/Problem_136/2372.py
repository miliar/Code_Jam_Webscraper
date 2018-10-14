import sys

T = int(sys.stdin.readline().rstrip())

for caseno in range(T):
    c,f,x = map(float, sys.stdin.readline().split())

    curr_rate = 2.0
    time_cf = 0.0

    min_so_far = base_time = x / curr_rate

    while True:
        time_cf += 1 / curr_rate
        curr_rate += f
        new_time = c * time_cf + x / curr_rate
        if new_time < min_so_far:
            min_so_far = new_time
        else:
            break

    print "Case #%d: %.7f" % (caseno + 1, min_so_far)
