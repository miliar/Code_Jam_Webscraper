fin = open("A-large.in", "r")
fout = open("A-large.out", "w")

T = int(fin.readline())

for t in xrange(T):
    N = int(fin.readline())
    wires = []
    for n in xrange(N):
        wires.append([int(i) for i in fin.readline().split()])
    intersections = 0
    for i in xrange(N):
        for j in xrange(i + 1, N):
            if wires[i][0] > wires[j][0]:
                if wires[i][1] < wires[j][1]:
                    intersections += 1
            elif wires[i][1] > wires[j][1]:
                intersections += 1
    fout.write("Case #%i: %i\n" % (t + 1, intersections))

fin.close()
fout.close()
