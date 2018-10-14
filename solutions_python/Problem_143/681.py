import sys

num_cases = int(sys.stdin.readline())
f = open('lottery.txt', 'w')

for n in range(0, num_cases):
    line = sys.stdin.readline()
    inputs = line.split()
    A = int(inputs[0])
    B = int(inputs[1])
    C = int(inputs[2])

    count = 0
    for i in range(0, A):
        for j in range(0, B):
            if i & j <= C - 1 and i & j >= 0:
                count += 1
    f.write('Case #%d: %s\n' % (n+1, count))
