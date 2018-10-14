#!/usr/bin/python

from decimal import *

try:
        with open("B-large.in") as inFile, open("output.txt", "w") as outFile:
                cases = int(inFile.readline().strip())
                for c in range(cases):
                        outFile.write("Case #" + str(c+1) + ": ")
                        info = inFile.readline().split(" ")
                        costFarm = Decimal(info[0].strip())
                        farmBonus = Decimal(info[1].strip())
                        xWin = Decimal(info[2].strip())
                        rate = Decimal(2)
                        elapsed = Decimal(0)
                        win = False
                        while win == False:
                                endTime = xWin/rate
                                farmTime = costFarm / rate
                                if endTime > farmTime + (xWin/(rate+farmBonus)):
                                        rate = rate + farmBonus
                                        elapsed = elapsed + farmTime
                                else:
                                        elapsed = elapsed + endTime
                                        win = True
                        outFile.write(str(elapsed.quantize(Decimal("0.0000001"), rounding=ROUND_HALF_UP)) + "\n")
except IOError as err:
        print(str(err))

