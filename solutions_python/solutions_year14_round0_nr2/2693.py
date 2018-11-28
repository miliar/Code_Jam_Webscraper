
T = int(raw_input())

for case in range(1, T+1):
    C, F, X = map(float, raw_input().split())

    time_taken = 0.0
    rate = 2.0 # 2 cookie per second

    best_time = X / rate
    while True:
        time_taken += C / rate
        rate += F
        expected_time = time_taken + (X/rate)
        if expected_time < best_time:
            best_time = expected_time
        else:
            break

    print "Case #%d: %.7f" % (case, best_time)
