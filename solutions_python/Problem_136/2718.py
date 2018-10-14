#!/usr/bin/env python
import fileinput
import sys


def shouldBuyFarm(cookieRate, farmCost, farmRate, cookiesToWin):
    withoutFarm = cookiesToWin / cookieRate
    withFarm = (farmCost / cookieRate) + (cookiesToWin / (cookieRate + farmRate))
    return withFarm < withoutFarm


def main():

    infile = fileinput.input()
    numCases = int(infile.readline())

    for case in range(1, numCases+1):
        sys.stdout.write("Case #{}: ".format(case))
        farmCost, farmRate, cookiesToWin = [float(x) for x in infile.readline().strip().split()]
        cookieRate = 2.0
        time = 0.0

        while shouldBuyFarm(cookieRate, farmCost, farmRate, cookiesToWin):
            time += farmCost / cookieRate
            cookieRate += farmRate
 
        time += cookiesToWin / cookieRate
        print time

if __name__ == "__main__":
    main()
