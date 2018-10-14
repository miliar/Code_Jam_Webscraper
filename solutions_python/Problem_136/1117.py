import sys

lines = sys.stdin.readlines()
T = int(lines[0])
for t in range(1, T + 1):
    time = 0
    rate = 2
    C, F, X = map(float, lines[t].split())
    while (X / rate) > (X / (rate + F) + C / rate):
        time += C / rate
        rate += F
    time += X / rate
    print('Case #{0}: {1:.7f}'.format(t, time))

