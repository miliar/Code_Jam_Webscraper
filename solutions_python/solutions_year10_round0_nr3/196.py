import sys

T = int(raw_input())

for x in xrange(T):
    R, k, N = map(int, raw_input().split(' '))
    groups = map(int, raw_input().split(' '))

    y = 0
    i = 0
    r = 0
    while r < R:
        ride_people = 0
        ride_groups = 0
        while ride_people <= k:
            if ride_people + groups[i] <= k:
                ride_people += groups[i]
                ride_groups += 1
                i = (i + 1) % N
                if ride_groups == N:
                    break
            else:
                break
        y += ride_people

        r += 1

        if i == 0:
            sys.stderr.write("x:%d, r:%d, R:%d, y:%d\n" % (x+1, r, R, y))
            mult = R / r
            y *= mult
            r *= mult

    print "Case #%d: %d" % (x+1, y)

        
                    
                
        
