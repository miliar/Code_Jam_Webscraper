
import sys

T = int(sys.stdin.readline())

for i in range(0, T):
    tokens = sys.stdin.readline().split()
    pancakes = list(tokens[0])
    K = int(tokens[1])

    count = 0
    for j in range(0, len(pancakes) - K + 1):
        if pancakes[j] == '-':
            count += 1
            for k in range(0, K):
                if pancakes[j + k] == '-':
                    pancakes[j + k] = '+'
                else:
                    pancakes[j + k] = '-'

    if '-' in pancakes:
        print("CASE #%d: IMPOSSIBLE" % (i+1))
    else:
        print("CASE #%d: %d" % ((i+1), count))



