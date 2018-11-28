#!/usr/bin/env python3


def main():
    t = int(input())

    for x in range(1, t + 1):
        d, n = map(int, input().split(" "))
        horses = []
        for z in range(0, n):
            k, s = map(int, input().split(" "))
            horses.append({'k': k, 's': s})
        y = getSpeed(d, horses)
        print("Case #{}: {}".format(x, y))


def getSpeed(d, horses):
    arrivals = [(d - h['k']) / h['s'] for h in horses]
    lastArrival = max(arrivals)
    return d/lastArrival


main()
