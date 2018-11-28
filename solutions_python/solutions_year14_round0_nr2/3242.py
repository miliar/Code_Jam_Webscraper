#!/usr/bin/python

def solve_n(case, C, F, X):
    t = 0.0 # Time stamp
    cc = 0.0 # Number of cookies
    cookie_rate = 2.0
    solved = False
    while not solved:
        time_to_next_event = C / cookie_rate
        ## Will I solve in this round
        time_to_solve = t + (X - cc) / cookie_rate
        if cc + cookie_rate * time_to_next_event >= X:
            t += (X - cc)/cookie_rate
            break
       
        cc += cookie_rate * time_to_next_event
        t += time_to_next_event
        buy_cookie = True
        ## Should I buy a cookie?
#        print "Before Buy cookies: %0.7f at t: %0.7f" % (cc, t)
        if buy_cookie:
            cc -= C
            cookie_rate += F
#        print "After Buy cookies: %f at t: %0.7f, rate: %0.7f" % (cc, t, cookie_rate)
        new_time_to_solve = t + (X - cc) / cookie_rate
#        print time_to_solve, new_time_to_solve
        if new_time_to_solve > time_to_solve:
            t = time_to_solve
            break

    print "Case #%d: %0.7f" % (case, t)

def solve(ip):
    count = int(ip.readline())
#    solve_n(-1, 500, 4.0, 2000.0)
    for case in range(count):
        C, F, X = map(float, ip.readline().split())
        solve_n(case + 1, C, F, X)

if __name__ == "__main__":
    import sys
    solve(open(sys.argv[1], "r"))

