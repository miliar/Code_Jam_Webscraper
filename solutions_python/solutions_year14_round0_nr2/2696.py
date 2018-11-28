rl = raw_input

cases = int(rl())
for cc in xrange(cases):
    cost, additional, target = map(float, rl().strip().split())
    best = target / 2.0

    time_spent = 0.0
    speed = 2.0
    while True:
        if time_spent >= best: break
        best = min(best, time_spent + target / speed)
        # get one more farm
        time_spent += cost / speed
        speed += additional

    print 'Case #%d: %.7lf' % (cc+1, best)
