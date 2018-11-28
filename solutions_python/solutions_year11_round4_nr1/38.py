

import sys
stin = sys.stdin

T = int(stin.readline())

for tcase in range(T):
    line = stin.readline()
    X, S, R, t, N = map(int, line.split())

    ws = []

    wdist  = 0
    for n in range(N):
        B, E, w = map(int, stin.readline().split())
        ws.append((w, B, E))
        wdist += (E - B)

    ws.append((0, 0, X - wdist))
    ws.sort()

    
    seconds = 0
    dist_covered = 0
    for w, B, E in ws:
        dist = E - B
        speed = w + R
        time_required = dist / (0.0 + speed)
        if time_required < t:
            t -= time_required
            dist_covered += dist
            seconds += time_required
            continue
        else:
            time_ran = t
            t = 0
            dist_ran = speed * time_ran
            dist_walk = dist - dist_ran
            time_walked = dist_walk / (w + S + 0.0)
            seconds += time_ran + time_walked
            dist_covered += dist

    

    print "Case #%d: %.10f" % (tcase+1, seconds)
