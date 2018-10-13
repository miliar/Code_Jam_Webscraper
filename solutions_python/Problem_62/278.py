def read(filename):
    f = open(filename)
    t = int(f.readline())

    for i in xrange(t):
        n = int(f.readline())
        coords = []
        for j in xrange(n):
            a, b = map(int, f.readline().split(' '))
            coords.append((a, b),)
        yield i, coords


def output(i, coords):
    result = 0
    for p1 in xrange(len(coords)):
        for p2 in xrange(p1 + 1, len(coords)):
            (a1, b1) = coords[p1]
            (a2, b2) = coords[p2]
            
            if ((a1 > a2) & (b1 < b2) | (a1 < a2) & (b1 > b2)) :
                result += 1

    return 'Case #%i: %i\n' % (i + 1, result)

fout = open('result.txt', 'w')

for data in read('A-large.in'):
    fout.write(output(*data))
