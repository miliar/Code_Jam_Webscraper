def hm(s):
    h,m = map(int, s.split(':'))
    return h*60 + m

def solve(t, a, b):
    a = triptime(t, a)
    b = triptime(t, b)
    na = len(a)
    nb = len(b)
    return na - count_turnaround(b, a), nb - count_turnaround(a, b)

def count_turnaround(a, b):
    c = 0
    b = sorted(b)
    for a1, a2 in sorted(a, key=lambda(x,y): (y,x)):
        for i in xrange(len(b)):
            if a2 <= b[i][0]:
                c += 1
                del b[:i+1]
                break
    return c

def triptime(t, tbl):
    ret = []
    for tline in tbl:
        s, e = tline.split()
        ret.append([hm(s), hm(e)+t])
    return ret



def main(in_, out):
    N = int(in_.next())
    for i in range(N):
        T = int(in_.next())
        NA, NB = map(int, in_.next().split())
        A = [in_.next().rstrip() for j in xrange(NA)]
        B = [in_.next().rstrip() for j in xrange(NB)]
        a, b = solve(T, A, B)
        print >>out, 'Case #%d: %d %d' % (i+1, a, b)

if __name__ == '__main__':
    import sys
    main(sys.stdin, sys.stdout)
