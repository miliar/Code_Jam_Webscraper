import math

size = 'small'
fi = file('A-%s-attempt1.in' % size, 'rb')
fo = file('A-%s.out' % size, 'wb')

def read_int():
    return int(fi.readline().rstrip('\n'))

def read_int_array():
    return [int(i) for i in fi.readline().rstrip('\n').split(' ')]

def read_str_array():
    return fi.readline().rstrip('\n').split(' ')

def paint_circle(r):
    return (r+1)*(r+1) - r*r

T = read_int()
for n in xrange(T):
    r, p = read_int_array()
    print r, p

    a = (r+1)*(r+1) - r*r
    print a
    i = 0
    while (p > 0):
        p = p - a
        if p < 0: break
        a = a + 4
        i = i + 1

    print i
    output = 'Case #%d: %d\n' % (n+1, i)
    fo.write(output)

fi.close()
fo.close()