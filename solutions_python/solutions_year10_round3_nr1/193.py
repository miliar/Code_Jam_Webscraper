import sys
number = int(sys.stdin.readline().rstrip('\n'))

def cross(wires, A, B):
    c = 0
    for w in wires:
        if (A < w[0] and B > w[1]) or (A > w[0] and B < w[1]):
            c += 1
    return c

for i in range(number):
    l = sys.stdin.readline().rstrip('\n').split(' ')
    N = int(l[0])
    wires = []
    crosses = 0
    for j in range(N):
        l = sys.stdin.readline().rstrip('\n').split(' ')
        crosses += cross(wires, int(l[0]), int(l[1]))
        wires.append((int(l[0]), int(l[1])))
    print "Case #" + str(i+1) + ": " + str(crosses)
