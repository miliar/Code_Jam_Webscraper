import sys
from decimal import *

def main():
    with open(sys.argv[1]) as inputFile:
        outputFile = open('cookie_output.txt', 'w')

        numberCases = int(inputFile.readline())
        for x in range(0, numberCases):
            inputVals = inputFile.readline().split()
            C = Decimal(inputVals[0])
            F = Decimal(inputVals[1])
            X = Decimal(inputVals[2])

            bake_rate = Decimal(2)
            total_time = Decimal(0)
            while worth_buying_farm(C, F, X, bake_rate, total_time):
                total_time += C / bake_rate
                bake_rate += F

            total_time += X / bake_rate

            outputFile.write('Case #' + str(x + 1) + ': ' + "{:.7f}".format(total_time) + '\n')
        outputFile.close()


def worth_buying_farm(C, F, X, bake_rate, total_time):
    time_build_farm = C / bake_rate
    time_bake_X_cookies = X / (bake_rate + F)
    time_bake_X_cookies_no_farm = X / bake_rate
    if (total_time + time_build_farm + time_bake_X_cookies) < (total_time + time_bake_X_cookies_no_farm):
        return True
    return False


if __name__ == "__main__":
    main()