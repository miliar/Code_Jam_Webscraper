from sys import stdin

N = int(stdin.readline())
for case in range(1, N + 1):
    (pancake_string, K) = tuple(stdin.readline().split(' '))
    pancakes = map(lambda c: c == '+', pancake_string)
    K = int(K)

    count = 0
    for i in range(0, len(pancakes) - K + 1):
        if not pancakes[i]:
            count += 1
            for j in range(i, i + K):
                pancakes[j] = not pancakes[j]

    for i in range(len(pancakes) - K, len(pancakes)):
        if not pancakes[i]:
            count = -1

    if count == -1:
        print("Case #%d: IMPOSSIBLE" % case)
    else:
        print("Case #%d: %d" % (case, count))

