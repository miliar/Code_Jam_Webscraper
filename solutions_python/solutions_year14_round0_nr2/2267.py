test_cases = int(raw_input())

def get_answer(c, f, x):
    # If c > x, just shut up and wait till x:
    rate = float(2)
    if c>=x:
        return x/rate
    time = 0
    while True:
        normal_time = x/float(rate)
        expected_time = c/float(rate) + x/float(rate+f)
        if expected_time <= normal_time:
            time += float(c)/rate
            rate += float(f)
        else:
            time += float(normal_time)
            return time

for test in range(test_cases):
    C, F, X = raw_input().strip().split(' ')
    C = float(C.strip())
    F = float(F.strip())
    X = float(X.strip())

    a = get_answer(C, F, X)

    print 'Case #%d: %f' % (test+1, a)