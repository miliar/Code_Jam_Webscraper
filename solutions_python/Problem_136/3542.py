#!/usr/bin/python

if __name__ == "__main__":
    testcases = int(input())

    for case in range(1, testcases + 1):
        C, F, X = [ float(n) for n in input().split()]
        cookie_gen = 2.0
        sum_time = 0.0
        while True:
            current_win_time = X / cookie_gen
            candidate_win_time = (X) / (cookie_gen + F)
            farm_wait = ( C / cookie_gen ) 
            if (candidate_win_time+farm_wait) < current_win_time:
                sum_time = sum_time + ( C / cookie_gen) 
                cookie_gen = cookie_gen + F
            else:
                sum_time = sum_time + current_win_time
                break

        print("Case #%d: %s" % (case, sum_time))
        

