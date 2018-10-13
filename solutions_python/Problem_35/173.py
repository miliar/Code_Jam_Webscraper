from string import lowercase

def memoize(f):
    d = {}
    def g(*args):
        if args not in d:
            d[args] = f(*args)
        return d[args]
    return g

def ints():
    return map(int,raw_input().split())

def main():
    T,  = ints()

    for case in xrange(T):
        H,W = ints()

        rs = set(xrange(H))
        cs = set(xrange(W))

        def nbrs(r,c):
            for (dr,dc) in (-1,0),(0,-1),(0,1),(1,0): # N,W,E,S
                yield (r,c)
                if r+dr in rs and c+dc in cs:
                    yield (r+dr,c+dc)

        m = [ints() for _ in rs]

        @memoize
        def shed(r,c):
            n = list(nbrs(r,c))
            min_ = min(m[r_][c_] for (r_,c_) in n)
            for (r_,c_) in n:
                if m[r_][c_] == min_:
                    if (r_,c_) != (r,c):
                        return shed(r_,c_)
                    else:
                        return (r,c)

        print "Case #%s:" % (case+1)
        sheds = {}
        max_shed = 0
        for r in xrange(H):
            for c in xrange(W):
                s = shed(r,c)
                if s not in sheds:
                    sheds[s] = max_shed
                    max_shed += 1
                print lowercase[sheds[s]],
            print

if __name__ == '__main__':
    main()
