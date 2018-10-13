
def if_cross(wire1, wire2):
    if wire1[0] < wire2[0] and wire1[1] > wire2[1]:
        return True

    if wire1[0] > wire2[0] and wire1[1] < wire2[1]:
        return True

    return False

f = file('A-large.in')
T = int(f.readline())
TEMPLATE = "Case #%d: %d"

for i in range(T):
    N = int(f.readline())

    wires = []
    cross = 0

    for j in range(N):
        wires.append(map(int, f.readline().split()))

    for w1 in range(len(wires)):
        for w2 in range(w1, len(wires)):
            if if_cross(wires[w1], wires[w2]):
                cross = cross + 1

    print TEMPLATE % (i + 1, cross)

