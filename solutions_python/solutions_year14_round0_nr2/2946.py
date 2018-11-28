def solve(C, F, X):

    frequency = 2.0
    
    total_time = 0.0
    time_to_goal = X/frequency
    time_to_farm = C/frequency

    while time_to_goal - time_to_farm > C/F:
        
        total_time += time_to_farm
        frequency += F
        time_to_farm = C/frequency
        time_to_goal = X/frequency

    return total_time + time_to_goal

if __name__ == '__main__':

    T = int(raw_input())
    for t in xrange(T):
        C,F,X = map(float, raw_input().split())
        print u"Case #%d: %s" % (t+1, solve(C,F,X))


