
i = open("in.txt", "r")
o = open("out.txt", "w")

Tests = int(i.readline())
for test in range(Tests):
    N = int(i.readline())
    wires = []
    for x in range(N):
        wires.append(i.readline().split())
        wires[x][0] = int(wires[x][0])
        wires[x][1] = int(wires[x][1])
    wires.sort();
    res = 0;
    for x in range(N):
        res = res + len([y for y in wires[x+1:] if y[1]<wires[x][1]])
            
    o.write("Case #{0}: {1}\n".format(test+1, res))

o.close()
i.close()
