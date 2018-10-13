import sys
import psyco
psyco.full()

def main(ifile):
    T = int(ifile.readline())
    for i in range(T):
        foo(i+1,ifile)

def foo(idx, ifile):
    H,W = [int(x) for x in ifile.readline().split()]
    a = []

    for i in range(H):
        a.append([int(x) for x in ifile.readline().split()])

    b = [[None]*W for i in range(H)]
    tt = []
    for i in range(H):
        for j in range(W):
            t = a[i][j]
            for x in [(-1, 0), (0, -1), (0, 1), (1,0)]:
                ii = i + x[0]
                jj = j + x[1]
                if ii < 0 or ii >= H:
                    continue
                if jj < 0 or jj >= W:
                    continue
                if a[ii][jj] < t:
                    t = a[ii][jj]
                    b[i][j] = (ii,jj)
            if b[i][j] is None:
                tt.append((i,j))

    c = [[None]*W for i in range(H)]
    for x in tt:
        c[x[0]][x[1]] = x
        q = [x]
        while q:
            t = q.pop()
            for y in [(1, 0), (0, 1), (0, -1), (-1,0)]:
                t2 = (t[0]+y[0], t[1]+y[1])
                if t2[0] < 0 or t2[0] >= H:
                    continue;
                if t2[1] < 0 or t2[1] >= W:
                    continue
                if b[t2[0]][t2[1]] == t:
                    c[t2[0]][t2[1]] = x
                    q.append(t2)

    m = {}
    next = 'a'
    print 'Case #%d:' % idx
    for i in range(H):
        for j in range(W):
            t = c[i][j]
            if t not in m:
                m[t] = next
                next = chr(ord(next)+1)
            print m[t],
        print

main(sys.stdin)





            



    
