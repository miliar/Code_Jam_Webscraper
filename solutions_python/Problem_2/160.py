def solve(T, atob, btoa):
    a_trains_coming = load(btoa, T)
    b_trains_coming = load(atob, T)

    a_needs = check(atob, a_trains_coming)
    b_needs = check(btoa, b_trains_coming)

    return (a_needs, b_needs)

def check(schedule, trains_coming):
    n = 0
    for train in schedule:
        if not is_coming(train, trains_coming):
            n+=1
    return n

def is_coming(train, trains_coming):
    for i, train_coming in enumerate(trains_coming):
        if train[0] >= train_coming:
            trains_coming.pop(i)
            return True
    return False


def load(schedule, T):
    trains_coming = []
    for train in schedule:
        trains_coming.append(train[1]+T)
    trains_coming.sort()
    return trains_coming

def to_minutes(time_str):
    time = map(int, time_str.split(":"))
    return time[0]*60 + time[1]

def read_input():
    from sys import stdin
    N = int(stdin.readline())
    n_of_trains = []
    for n in range(N):
        T = int(stdin.readline())
        NA, NB = map(int, stdin.readline().strip().split())
        def read_trains(N):
            trains = [ map(to_minutes, stdin.readline().strip().split()) for i in range(N) ]
            trains.sort()
            return trains
        atob = read_trains(NA)
        btoa = read_trains(NB)
        n_of_trains.append(solve(T, atob, btoa))

    for i, ntrains in enumerate(n_of_trains):
        print "Case #%d: %d %d" % (i+1, ntrains[0], ntrains[1])

read_input()
