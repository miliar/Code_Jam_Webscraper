from sys import stdin

T = int(stdin.readline())
for t in range(1, T+1):
    pancakes, K = stdin.readline().split()
    K = int(K)
    pancakes = [p for p in pancakes]
    flips = 0
    for i in range(len(pancakes) - K + 1):
        if pancakes[i] == '-':
            flips += 1
            for j in range(i, i + K):
                pancakes[j] = '-' if pancakes[j] == '+' else '+'
    result = "IMPOSSIBLE"
    if sum([1 for p in pancakes if p == '+']) == len(pancakes):
        result = str(flips)
    print "Case #%d: %s" % (t, result)
