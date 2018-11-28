from math import pi

t = int(raw_input())

for case in range(t):
    n, k = map(int, raw_input().split())
    pancakes = []
    for i in range(n):
        pancakes.append(map(int, raw_input().split()))
    pancakes = sorted(pancakes)
    while len(pancakes) > k:
        min_contrib = 10**32
        min_index = -1
        for i in range(len(pancakes)):
            contrib = 2 * pi * pancakes[i][0] * pancakes[i][1]
            if i == len(pancakes) - 1:
                contrib += (pi * pancakes[i][0]**2) - (pi * pancakes[i - 1][0]**2)
            if contrib < min_contrib:
                min_contrib = contrib
                min_index = i
        del pancakes[min_index]
    ans = pi * pancakes[-1][0]**2
    for p in pancakes:
        ans += 2 * pi * p[0] * p[1]
    print "Case #" + str(case + 1) + ": " + str(ans)
