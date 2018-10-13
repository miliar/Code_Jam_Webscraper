#!/usr/bin/python

import sys

def getCFX(line):
    str_CFX = line.split()

    result = []
    for v in str_CFX:
        result.append(float(v))
    return result

# C = farm cost
# F = farm production
# X = final
def getResult(C, F, X):
    farm_count = 0
    consum_sec = 0

    while True:
        production = 2 + (farm_count * F)

        last_sec = X / production
        # buy farm sec     # last_sec
        buy_farm_sec = C / production
        next_step_last_sec = X / (2 + ((farm_count+1) * F))

        if last_sec <= buy_farm_sec + next_step_last_sec:
            return consum_sec + last_sec
        else:
            farm_count = farm_count + 1
            consum_sec = consum_sec + buy_farm_sec 
    

# MAIN
test_count = int(sys.stdin.readline().strip())

for this_round in range(test_count):
    line = sys.stdin.readline().strip()

    C, F, X = getCFX(line)

    result = getResult(C, F, X)

    print("Case #%d: %.7f" % (this_round+1, result))

