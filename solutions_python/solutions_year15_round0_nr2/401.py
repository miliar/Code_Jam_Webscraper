# -*- coding: utf-8 -*-

from math import ceil
def case(pancakes):
    maxpancake = max(pancakes)
    time = maxpancake
    pancakes = sorted(pancakes, key=lambda x: -x)
    for amountofpancake in xrange(1, maxpancake + 1):
        take = 0
        for pancake in pancakes:
            if pancake <= amountofpancake:
                break
            take += int(ceil(float(pancake) / amountofpancake)) - 1

        if take + amountofpancake < time:
            time = take + amountofpancake
    
    return time        

def fromStdin():
    while True:
        yield raw_input()

def main():
    feed = fromStdin()
    T = int(next(feed))
    for i in xrange(T):
        D = int(next(feed))
        P = [int(j) for j in next(feed).split()]
        time = case(P)
        print "Case #{}: {}".format(i+1, time)

if __name__ == "__main__":
    main()
