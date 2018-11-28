import math

t = int(raw_input())

for case in range(t):
    n, k = map(int, raw_input().split())
    u = float(raw_input())
    probs = map(float, raw_input().split())
    while u > 10**(-6):
        least = 1
        second_least = 1
        min_indices = []
        for i in range(len(probs)):
            if probs[i] < least:
                second_least, least = least, probs[i]
                min_indices = [i]
            elif probs[i] == least:
                min_indices.append(i)
            if least < probs[i] < second_least:
                second_least = probs[i]
        if (second_least - least) * len(min_indices) <= u:
            u -= (second_least - least) * len(min_indices)
            for i in min_indices:
                probs[i] += (second_least - least)
        else:
            for i in min_indices:
                probs[i] += (u / len(min_indices))
            u = 0
    print "Case #" + str(case + 1) + ": " + str(reduce(lambda x, y: x * y, probs))

