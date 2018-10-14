#!/usr/bin/env python
import sys
sys.setrecursionlimit(10000)


def main():
    f = sys.stdin
    cases = int(f.readline())
    for case in range(1, cases+1):
        FARM_COST, FARM_CPS, TARGET_COOKIES = [float(n) for n in f.readline().split(" ")]
        
        def buy_farm_or_finish(cookies, cps):
            remaining_cookies = TARGET_COOKIES - cookies
            base_time = remaining_cookies / cps
            wait_for_farm_time = FARM_COST / cps
            hypotetical_new_cps = cps + FARM_CPS
            if  wait_for_farm_time + (remaining_cookies / hypotetical_new_cps) < base_time:
                return wait_for_farm_time + buy_farm_or_finish(cookies, hypotetical_new_cps)
            else:
                return base_time

        time = buy_farm_or_finish(0, 2)
        
        print "Case #%s: %.7f" % (case, time)
            
if __name__ == "__main__":
    main()
