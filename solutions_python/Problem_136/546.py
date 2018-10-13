import sys

T = int(input())
test = 1

sys.setrecursionlimit(15000)


while test <= T:
    print("Case #" + str(test) + ": ", end="")
    test += 1

    inputs = [float(a) for a in input().split()]
    C = inputs[0]
    F = inputs[1]
    X = inputs[2]

    rate = 2
    time = 0

    while X/rate > C/rate + X/(rate+F):
        time += C/rate
        rate += F
    time += X/rate

    print(time)
