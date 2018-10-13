#!/usr/bin/python

PRECISION = 7

class Case:
    def __init__(self, data, index):
        self.index = index

        data = data.split(' ')

        c = float(data[0])
        f = float(data[1])
        x = float(data[2])

        rate = 2.0
        self.time = 0.0

        while (True):
            timeUntilFarm = c / rate
            timeUntilWin = x / rate

            rate += f

            timeUntilWinWithOneMoreFarm = timeUntilFarm + (x / rate)

            # If it makes more sense to buy a farm, we purchase one.
            if timeUntilWinWithOneMoreFarm < timeUntilWin:
                self.time += timeUntilFarm
            else:
                self.time += timeUntilWin
                self.time = round(self.time, PRECISION)
                break;

    def getAnswer(self):
        return "Case #{}: {}\n".format(self.index, self.time)

import sys

# Read the input from stdin.
data = sys.stdin.readlines()

# Split the input into the number of cases and the cases themselves.
T, cases = int(data[0]), data[1:]

# Process the cases, retrieve the answers, and print them.
msg = ""
for i in range(0, T):
    msg += Case(cases[i], i + 1).getAnswer()

print(msg)
