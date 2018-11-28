T = int(raw_input())

for t in xrange(T):
    C, F, X = map(float, raw_input().split())
    P = 2

    cookies = 0.0
    time = 0.0

    while cookies < X:

        if cookies < C:
            goal = min(C, X) - cookies
            time += goal / P
            cookies += goal
            continue

        est1 = (X - cookies) / P
        est2 = (X - (cookies - C)) / (P + F)

        if est1 <= est2:
            time += (X - cookies) / P
            cookies = X
        else:
            cookies -= C
            P += F

    print 'Case #%d: %f' % (t+1, time)
            
