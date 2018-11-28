T = int(raw_input())

def time_to(goal, rate):
    return goal/rate

for i in range(1, T + 1):
    C, F, X = map(float, raw_input().split(' '))
    rate = 2.0
    
    times = []
    while time_to(X, rate) > time_to(X, rate + F) + time_to(C, rate):
        times.append(time_to(C, rate))
        rate += F
    times.append(time_to(X, rate))
    print('Case #%d: %.7f' % (i, sum(times)))
