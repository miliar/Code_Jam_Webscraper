T = int(raw_input())

for case in xrange(1, T+1):
    X, S, R, t, N = map(int, raw_input().split())

    walkways = []
    distance_left = float(X)
    for i in xrange(N):
        B, E, w = map(int, raw_input().split())
        dist = float(E-B)
        walkways.append((float(w),dist))
        distance_left -= dist
    walkways.append((0.0, distance_left))

    walkways.sort(reverse=True)
    #print walkways

    totaltime = 0.0

    while walkways:
        currentww = walkways[-1]
        del walkways[-1]
        dist = currentww[1]
        if t > 0.0:
            tempt = dist/(currentww[0]+R)
            if tempt > t:
                tempd = dist - t*(currentww[0] + R)
                tempt = t + (tempd)/(currentww[0]+S)
                t = 0.0
            else:
                t -= tempt
            totaltime += tempt
        else:
            totaltime += dist/(currentww[0]+S)

    print "Case #%d: %.6f"%(case, totaltime)


