import datetime

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    k, s = input().split(" ")
    s = int(s)
    pc = [True if c == '+' else False for c in k]
    total = 0
    for z in range(len(k) - s + 1):
        if pc[z]:
            continue
        total += 1
        for y in range(z, z + s):
            pc[y] = not pc[y]

    ex = True

    for z in range(len(k)-1, len(k)-s-1, -1):
        ex = ex and pc[z]

    print("Case #"+str(i)+": "+ ("IMPOSSIBLE" if not ex else str(total) ))