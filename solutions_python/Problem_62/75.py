
for case in range(1, int(input()) + 1):
    wires = []
    for _ in range(int(input())):
        wires.append(tuple(map(int, input().split())))
    i = 0
    for x1,y1 in wires:
        i += sum(1 for x2,y2 in wires if x1 < x2 and y1 > y2)
    print('Case #%d: %d' % (case, i))
