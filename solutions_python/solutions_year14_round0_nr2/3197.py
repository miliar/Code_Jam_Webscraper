#!/usr/bin/env python3

def compute_optimal_time(farm_price, farms_cookies, target, time=0, current_rate=2.0, cookies=0.0):
    while target != 0:        
        if cookies < farm_price:
            time   += farm_price/current_rate
            cookies = farm_price
            target -= farm_price
        elif cookies >= farm_price:
            if (target + farm_price)/(current_rate + farms_cookies) < (target/current_rate):
                 cookies -= farm_price
                 target += farm_price
                 current_rate += farms_cookies
            else:
                cookies += target
                time += target/current_rate
                target = 0
    return time


def main():
    for n in range(int(input())):
        C, F, X = [float(x) for x in input().split()]
        print("Case #{0}: {1}".format(n+1 ,round(compute_optimal_time(C, F, X), 7)))
    
if __name__ == '__main__':
    main()
