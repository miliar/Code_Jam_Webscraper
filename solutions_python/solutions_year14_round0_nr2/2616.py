#!/usr/bin/env python

T = int(raw_input().strip())

def solve(C, F, X, production_rate=2):
    time_taken = 0
    production_rate = 2

    while True:
        #print
        #print time_taken, production_rate
        # How about not buying a cookie farm?
        ans1 = X/production_rate

        # How about buying one, then not?
        time_to_cookie_farm = C/production_rate
        ans2 = time_to_cookie_farm + X/(production_rate+F)

        if ans2 > ans1:
            # Time to leave!
            return time_taken + ans1

        time_taken += time_to_cookie_farm
        production_rate += F

for i in range(1, T+1):
    print ("Case #%d:" % i),

    C, F, X = [float(x) for x in raw_input().strip().split()]
    print solve(C, F, X)
