from sys import stdin

T = int(stdin.readline())

for case in xrange(T):

    X, S, R, t, N = map(int, stdin.readline().strip().split())
    S = float(S)   
    R = float(R)

    reached = 0 
    no_belt = 0
    legs = []
    for _ in xrange(N):
        B, E, w = map(int, stdin.readline().strip().split())
        no_belt += B - reached
        legs.append((w, E - B))
        reached = E

    no_belt += X - reached

    legs.sort()
    legs = [(0, no_belt)] + legs
    total_time = 0

    for speed, dist in legs:
        if t > 0:
            run_speed = speed + R
            run_dist = run_speed * t
            this_run_dist = min(dist, run_dist)
            dist -= this_run_dist
            run_time = this_run_dist / run_speed
            t -= run_time
            total_time += run_time
        if dist > 0:
            total_time += dist / (speed + S)

    print("Case #%d: %0.9f" % (case + 1, total_time))
