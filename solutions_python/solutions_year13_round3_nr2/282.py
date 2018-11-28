#/usr/bin/cython --embed -2 B.pyx
#/usr/bin/gcc -o B -I/usr/include/python2.7 B.c /usr/lib/libpython2.7.so
#./B
import sys
   
def tt(path, x, y, k):
    global A
    p = (x + k, y)
    if p not in A or len(A[p]) > k:
        A[p] = path + 'E'
        if k<25: tt(path + 'E', p[0], p[1], k+1)
    p = (x, y + k)
    if p not in A or len(A[p]) > k:
        A[p] = path + 'N'
        if k<25: tt(path + 'N', p[0], p[1], k+1)
    p = (x - k, y)
    if p not in A or len(A[p]) > k:
        A[p] = path + 'W'
        if k<25: tt(path + 'W', p[0], p[1], k+1)
    p = (x, y - k)
    if p not in A or len(A[p]) > k:
        A[p] = path + 'S'
        if k<25: tt(path + 'S', p[0], p[1], k+1)
    
    
def pre():
    global A
    A = dict()
    
    tt('', 0, 0, 1)
    
    sys.stderr.write('A=%d\n' % len(A))
    
def check(ans, cx, cy):
    k = 0
    x = 0
    y = 0
    for c in ans:
        k += 1
        if c == 'E':
            x += k
        elif c == 'N':
            y += k
        elif c == 'W':
            x -= k
        elif c == 'S':
            y -= k
    if x != cx or y != cy:
        sys.stderr.write('!! %d %d => %s\n' % (cx, cy, ans)) 
    else:
        sys.stderr.write('ok')
    
def q():
    global A
    x, y = map(int, sys.stdin.readline().split())

    p = (x, y)
    
    ans = A.get(p, '')
    check(ans, x, y)    
    return ans
    

pre()

T = int(sys.stdin.readline())
for t in range(T):
    print 'Case #%d: %s' % (t+1, q())
