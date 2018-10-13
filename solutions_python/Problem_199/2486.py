
def pancakes(cakes, k): 
    flips = 0
    for i in range(len(cakes)-k+1):
        if cakes[i] == -1:
            for j in range(i, i+k):
                cakes[j] *= -1
            flips += 1
    return all([cake == 1 for cake in cakes]), flips

with open('A-large.in', 'r') as fd:
    t = int(fd.readline())
    for l in range(1, t+1):
        line = fd.readline().split()
        cake_line = line[0]
        cakes = []
        for i in range(len(cake_line)):
            cakes.append(int(cake_line[i] + '1'))
        k = int(line[1])
        possible, flips = pancakes(cakes, k)
        if possible:
            print 'Case #%d: %d' % (l, flips)
        else:
            print 'Case #%d: Impossible' % l
