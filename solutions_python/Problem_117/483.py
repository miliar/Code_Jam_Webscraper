
def read_lawn(f):
    [r,c] = f.readline().split()
    r = int(r.strip())
    c = int(c.strip())

    l = [[int(x) for x in f.readline().split()] for i in range(0,r)]
    return (r,c,l)
        

def maxat(i, l):
    m = -1
    for x in l:
        m = max(x[i],m)
    return m

def check(r, c, l):
    rm = [max(l[i]) for i in range(0, r)]
    cm = [maxat(i, l) for i in range(0, c)]

    for rr in range(0, r):
        for cc in range(0, c):
            if l[rr][cc] < min(rm[rr], cm[cc]):
                return 'NO'
            if l[rr][cc] > 100 or l[rr][cc] < 1:
                return 'NO'
    return 'YES'

def main(f):
    count = int(f.readline())
    for i in range(1,count+1):
        (r,c,l) = read_lawn(f)
        print 'Case #%d: %s' % (i, check(r,c,l))

import sys

if __name__ == '__main__':
    main(sys.stdin) 


