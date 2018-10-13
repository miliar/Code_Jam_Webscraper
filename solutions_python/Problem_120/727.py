import sys

def area(n, r):
    add = (r + n + 1) ** 2
    sub = (r + n) ** 2
    return add - sub 

f = open(sys.argv[1], 'r')

T = int(f.readline())
for tt in range(T):
    r, t = [int(x) for x in f.readline().strip().split()]
    
    circles = 0
    
    i = 0
    while True:
        t -= area(i, r)
        if t < 0:
            break
        circles += 1
        i += 2
    
    print('Case #%d: %d' % (tt + 1, circles))

f.close()