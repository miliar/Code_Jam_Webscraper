def timeit(C, F, X):
    speed = 2.0
    elapsed = 0.0
    while True:
        time1 = X / speed
        if X < C:
            return elapsed + time1
        speed += F
        time2 = C / (speed - F) + X / speed
        if time1 < time2:
            return elapsed + time1
        else:
            elapsed += C / (speed - F)

for i in range(int(raw_input())):
    C, F, X = [float(f) for f in raw_input().split()]
    print('Case #%d: %.7f' % (i + 1, timeit(C, F, X)))
