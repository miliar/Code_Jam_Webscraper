#!/usr/bin/env python3
t = int(input())
for i in range(1, t + 1):
    pancakes, k = input().split(" ")
    k = int(k)
    pancakes = list(pancakes)
    numFlips = 0
    for j in range(0, len(pancakes) - (k - 1)):
        if pancakes[j] == "-":
            numFlips +=1
            for n in range(0, k):
                pancakes[j+n] = "+" if pancakes[j+n] == "-" else "-"
    # check if it worked
    successful = True
    # check the last k-1 places (i.e. if k=2 then check the last place)
    for j in range(len(pancakes) - (k - 1), len(pancakes)):
        if pancakes[j] != "+":
            successful = False
            break
    if not successful:
        numFlips = "IMPOSSIBLE"
    print("Case #{}: {}".format(i, numFlips))
