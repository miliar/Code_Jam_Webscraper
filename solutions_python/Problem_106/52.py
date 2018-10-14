def readstr():
    return buf.pop()

def readstrs():
    return buf.pop().split()

def readint():
    return int(readstr())

def readints():
    return [int(e) for e in readstrs()]

def readfloats():
    return [float(e) for e in readstrs()]

def get_t(a, t0, x):
    return t0 + t1(x, a)

def t1(d, a):
    return (2.0*d/a) ** 0.5

def test():
    print t1(1, 2.0)
    print t1(4, 2.0)
    print t1(9, 2.0)
    print t1(16, 2.0)
    print t1(25, 2.0)

#test()
#exit()

def min_dist(t0, other, a):
    return min(int(t < t0) or (get_t(a, t0, x) - t) for (t, x) in other)

def cut(d, other):
    ret = [(0.0, 0.0)]
    for (t, x) in other:
#        print (t, x)
        if x <= d:
            ret.append((t, x))
            continue
        t1, x1 = t, x
        t0, x0 = ret[-1]
        ret.append((
          (t0*(x1-d)-t1*(x0-d)) / (x1-x0)
        , d))
        break
    return ret

def solve():
    d, n, A = [f(x) for (f, x) in zip([float, int, int], readstrs())]
    other = cut(d, [tuple(readfloats()) for i in range(n)])
    acc = readfloats()
    ret = []
    for a in acc:
        t_min = 0.0
        t_max = 1000000.0
        eps = 0.0000001
        while True:
          try:
            t = (t_max + t_min) / 2
            if t_max - t_min < eps:
                break
            if min_dist(t, other, a) > 0:
                t_max = t
            else:
                t_min = t
          except:
            print t_min, t_max, min_dist(t)
            raise
        ret.append(t + t1(d, a))
#        print '; '.join('%f: %f' % (t_, min_dist(t_, other, a)) for t_ in [t - 0.1, t, t + 0.1])
    return '\n' + '\n'.join(str(t) for t in ret)

if __name__ == '__main__':
    from sys import stdin
    buf = []
    for line in stdin:
        buf.append(line)
    buf.reverse()
    N = int(buf.pop())

    for i in range(1, N+1):
        print 'Case #%d: %s' % (i, solve())
