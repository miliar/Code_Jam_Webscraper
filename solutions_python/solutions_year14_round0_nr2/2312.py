T = input()
for t in xrange(T):
    C, F, X = map(float, raw_input().split())
    result = float(X) / 2
    farm = 0.0
    total = 0.0
    speed = 2.0
    while True:
        total += C / speed
        speed += F
        
        candidate = total + X / speed
        if candidate <= result:
            result = candidate
        else:
            break
    
    print 'Case #{}: {}'.format(t + 1, result)
