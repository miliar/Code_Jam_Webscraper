INFINITY = float("inf")

T = int(raw_input())

for case_num in xrange(1, T + 1):
    C, F, X = map(float, raw_input().split())
    cookie_rate = 2.0
    time_until_now = 0.0
    best_time = INFINITY
    while True:
        if time_until_now > best_time:
            break

        total_time = time_until_now + X / cookie_rate
        if total_time < best_time:
            best_time = total_time

        time_until_now += C / cookie_rate
        cookie_rate += F

    print "Case #{}: {:.7f}".format(case_num, best_time)
