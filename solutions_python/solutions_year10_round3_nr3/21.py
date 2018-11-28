import sys
from collections import defaultdict as dd

def main(inp, out, log):
    xxx = ''
    for _ in xrange(512/2):
        xxx += '0'
        xxx += '1'
    arow = xxx 
    brow = '1' + xxx[:-1]
    
    T = int(inp.readline())
    tobin = lambda n: n>0 and tobin(n>>1).lstrip('0')+str(n&1) or '0'
    for t in xrange(T):
        M, N = map(int, inp.readline().split())
        log(M, N)
        def aug(r):
            for _ in range(len(r), N):
                r = '0' + r
            return r
        rows = map(lambda r: aug(tobin(int(inp.readline().strip(), 16))), xrange(M))

        def trycut(leftcol, toprow, dim):
            assert dim > 0
##            assert dim % 2 == 0
            t = map(lambda r:r[leftcol:leftcol+dim], rows[toprow:toprow+dim])
            if len(t) < dim:
                return False
            if len(t[0]) < dim:
                return False
            fst, snd = None, None
            if arow.startswith(t[0]):
                fst, snd = arow, brow
            elif brow.startswith(t[0]):
                fst, snd = brow, arow
            else:
                return False
            for r in xrange(0, dim, 2):
                if not fst.startswith(t[r]):
                    return False
                if r+1 < len(t):
                    if not snd.startswith(t[r+1]):
                        return False
            return True

        def makecut(leftcol, toprow, dim):
            for r in xrange(toprow, toprow+dim):
                rows[r] = rows[r][:leftcol] + 'x'*dim + rows[r][leftcol+dim:]

        res = dd(int)

        maxdim = min(N, M)
        while maxdim:
            target = 2
            possib = dd(list)
            for r in xrange(M):
                for c in xrange(N):
                    best = 0
                    for dim in xrange(target, maxdim + 1):
                        if not trycut(c, r, dim):
                            break
                        best = dim
                    if best >= target:
                        possib[best].append((r, c))
                        target = best
            if possib:
                dim, coords = sorted(possib.iteritems(), key=lambda (k, v):k)[-1]
                for r, c in coords:
                    if trycut(c, r, dim):
                        res[dim] += 1
                        makecut(c, r, dim)
                maxdim = dim
            else:
                maxdim = 0

        log("\n".join(rows))
        for row in rows:
            for c in row:
                if c != 'x':
                    res[1] += 1
        print "Case #%d: %d" % (t+1, len(res))
        for dim, count in sorted(res.iteritems(), key=lambda (k,_):k, reverse=True):
            print dim, count


if __name__ == "__main__":
    def makef(stream):
        def ans(*ss):
            if stream:
                for s in ss:
                    print >> stream, s,
                print >> stream
        return ans
    if not sys.argv[0]:
        main(open('sample.in'), makef(sys.stdout), makef(sys.stdout))
    else:
        main(sys.stdin, makef(sys.stdout), makef(None))
