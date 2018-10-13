def A():
    D, N = map(int, raw_input().strip().split())
    
    position, speed = [], []

    for _ in xrange(N):
    	p, s = map(int, raw_input().strip().split())
    	position.append(p)
    	speed.append(s)

    time = []

    for i in xrange(N):
    	time.append((D-position[i])/float(speed[i]))

    time = sorted(time)
    # print position
    # print speed
    # print time, D
    return D/time[len(time)-1]
for case in xrange(input()):
    result = A()
    print 'Case #%d: %0.6f' % (case+1,result)
