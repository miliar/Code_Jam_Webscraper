import math

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    n, k = [int(s) for s in input().split(" ")]
    u = float(input())
    cores = [float(s) for s in input().split(" ")]
    cores = sorted(cores)
    while u > 0:
        equalCores = 1
        index = 0
        increment = 0
        while index < len(cores) - 1 and cores[index] == cores[index + 1]:
            index += 1
            equalCores += 1
        if equalCores == len(cores):
            increment = u / len(cores)
        else:
            nextValue = cores[equalCores]
            if (nextValue - cores[0]) * equalCores <= u:
                increment = nextValue - cores[0]
            else:
                increment = u / equalCores
        for x in range(0, equalCores):
            cores[x] += increment
            u -= increment
    answer = cores[0]
    for x in range(1, len(cores)):
        answer *= cores[x]
    print("Case #%d: %f" % (i, answer))