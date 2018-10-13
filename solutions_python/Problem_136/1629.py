T = input()
for i in xrange(T):
    C, F, X = [float(j) for j in raw_input().split()]
    rate = 2.0
    min_time = X / rate
    current_time = C / rate
    while current_time < min_time:
        rate += F
        if current_time + X / rate < min_time:
            min_time = current_time + X / rate
        current_time += C / rate
    print 'Case #'+str(i+1)+': '+str(min_time)


