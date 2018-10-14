dxy = ((0, -1), (-1, 0), (1, 0), (0, 1))
m = dim = []

def minel(x, y):
    minval, minx, miny = m[y][x], x, y
    for u, v in dxy:
        newx, newy = (x + u), (y + v)
        if newx >= 0 and newx < dim[1] and newy >= 0 and newy < dim[0] and m[newy][newx] < minval:
            minval, minx, miny = m[newy][newx], newx, newy
    return (minx, miny)

file = open("B-large.in")
T = int(file.next())
for i in range(T):
    dim = [int(s) for s in file.next().split(' ')]
    m = [[] for j in range(dim[0])]
    for j in range(dim[0]):
        nums = file.next().split(' ')
        for k in nums:
            m[j].append(int(k))
    a = [['' for k in range(dim[1])] for j in range(dim[0])]
    c = 'a'
    for j in range(dim[0]):
        for k in range(dim[1]):
            x, y = k, j
            while True:
                (minx, miny) = minel(x, y)
                if a[miny][minx] != '' or (minx, miny) == (x, y):
                    x, y = minx, miny
                    break
                x, y = minx, miny
            a[j][k] = a[y][x]
            if a[j][k] == '':
                a[j][k] = c
                c = chr(ord(c) + 1)
            r, t = k, j
            while (r, t) != (x, y):
                (r, t) = minel(r, t)
                a[t][r] = a[j][k]
    print "Case #%i:" % (i + 1)
    for j in range(dim[0]):
        print ' '.join([a[j][k] for k in range(dim[1])])
file.close()
