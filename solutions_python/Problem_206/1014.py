def time(d, k, s):
    return (d - k)*1.0/s

t = int(raw_input().strip())
for ti in range(1,t+1):
    d,n = [int(x) for x in raw_input().strip().split(' ')]
    times = []
    for ni in range(n):
        k,s = [int(x) for x in raw_input().strip().split(' ')]
        times.append(time(d, k, s))
    times.sort(reverse = True)
    answer = d/times[0]    
            
    print 'Case #' + str(ti) + ': ' + str(answer)    