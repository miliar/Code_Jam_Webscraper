import sys
import math

if len(sys.argv) < 2:
    exit()

input = [line.strip() for line in open(sys.argv[1])]

file = open('cookieclickeroutput.txt', 'w')

T = int(input[0])

def calcWinTime(n, C, F, X):
    cpr = 2
    times = []
    time = 0
    for i in range(n - 2):
        time += C / cpr
        cpr += F
    for numFarms in range(n - 1, n + 1):
        times.append(time + X/cpr)
        time += C / cpr
        cpr += F
    return min(times)



for n in range(1, T + 1):
    C, F, X = list(map(float, input[n].split()))
    cpr = 2 #cookie production rate
    numFarms = math.ceil((-2/F + X/C))
    winTime = calcWinTime(numFarms, C, F, X)

    file.write("Case #{0}: {1:.7f}\n".format(n, winTime))


