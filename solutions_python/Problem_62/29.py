fin = open('A-large.in', 'r')
fout = open('A-large.out', 'w')

for t in range(int(fin.readline())):
    n = int(fin.readline())
    a, b = [], []
    for i in range(n):
        x, y = [int(z) for z in fin.readline().strip().split(' ')]
        a.append(x)
        b.append(y)

    intersections = 0
    for x in range(n):
        for y in range(x):
            if a[x] < a[y]:
                if b[x] > b[y]:
                    intersections += 1
            elif b[x] < b[y]:
                intersections += 1

    print('Case #', t+1, ': ', intersections, sep='', file=fout)

fin.close()
fout.close()
