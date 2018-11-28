for i in range(input()):
    N = input()
    results = {}
    for j in range(N):
        results[j] = raw_input()
    
    WP = {}
    for j in range(N):
        w = results[j].count('1')
        l = results[j].count('0')
        WP[j] = (w + 0.0) / (w+l)

    OWP = {}
    for j in range(N):
        avg = 0.0
        match = 0
        for k in range(N):
            if results[j][k] != '.':
                match += 1
                w = results[k].count('1')
                l = results[k].count('0')
                if results[k][j] == '1': w -= 1
                elif results[k][j] == '0': l -= 1
                avg += (w + 0.0)/(w + l)

        avg /= match                
        OWP[j] = avg
        
    OOWP = {}
    for j in range(N):
        avg = 0.0
        match = 0
        for k in range(N):
            if results[j][k] != '.':
                avg += OWP[k]
                match += 1
        avg /= match
        OOWP[j] = avg

    print 'Case #{0}:'.format(i+1)
    for j in range(N):
        rpi = 0.25 * WP[j] + 0.50 * OWP[j] + 0.25 * OOWP[j]
        print rpi

