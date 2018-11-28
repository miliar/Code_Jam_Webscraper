#!/usr/bin/python

from sys import stdin

def main():
    numsamples = int(stdin.readline())
    for i in range(1, numsamples + 1):
        ans = readpuzzle()
        print "Case #%d: %.7f" % (i, ans)

def readpuzzle():
    line = stdin.readline().strip()
    args = line.split(" ")
    C, F, X = [float(arg) for arg in args]
    rate = 2.0
    time = 0.0
    while True:
        without_farm = X / rate
        with_farm = C / rate + X / (rate + F)
        if without_farm < with_farm:
            return time + without_farm
        else:
            time += C / rate
            rate += F

if __name__ == "__main__":
    main()

