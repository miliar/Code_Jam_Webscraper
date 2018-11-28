f = open('C-small.in')
g = open('C-small-output.in', 'w')
T = int(f.readline())
x = 1
while T > 0:
    y = 0
    line = f.readline().split()
    A = int(line[0])
    B = int(line[1])
    while A < B:
        SA = str(A)
        k = 1
        o = []
        while k < len(SA):
            SAA = SA[k:] + SA[:k]
            if A <= int(SAA) <= B and int(SAA) != A and SAA not in o:
                y += 1
            o.append(SAA)
            k += 1
        A += 1
    if x != 1:
        g.write('\n')
    g.write('Case #{}: {}'.format(x, y))
    T -= 1
    x += 1
f.close()
g.close()
