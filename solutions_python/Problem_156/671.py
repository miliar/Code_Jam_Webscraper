import math

def c(target, value):
    return int(math.ceil((target-value)/value))

for t in range(int(input())):
    d = int(input())
    diners = sorted([int(x) for x in input().split()])
    index = 0

    results = {}
    min_time = float('inf')

    for value in range(1, diners[-1] + 1):
        results[value] = value + sum(c(x, value) for x in diners if x > value)
        min_time = min(min_time, results[value])

    print('Case #{0}: {1}'.format(t+1, min_time))
