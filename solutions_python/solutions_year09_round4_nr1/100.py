import psyco
psyco.full()

def val(l):
    cnt = 0
    for i in xrange(len(l)):
        if l[i] > i:
            cnt += 1

    return cnt

def solve():
    for case in xrange(input()):
        n = int(raw_input())

        m = []
        for _ in xrange(n):
            s = raw_input()
            p = 0
            for i in xrange(n):
                if s[i] == '1': p = i
            m += [p]

        m = tuple(m)

        best = {}
        best[m] = 0
        q = [m]
        res = -1
        while q:
            u = q[0]

            if val(u) == 0:
                res = best[u]
                break

            q = q[1:]

            for i in xrange(n - 1):
                nm = list(u)
                nm[i], nm[i+1] = nm[i+1], nm[i]
                nm = tuple(nm)

                if nm not in best or best[nm] > best[u] + 1:
                    best[nm] = best[u] + 1
                    q += [nm]

        print 'Case #%d: %d' % (case+1, res)

solve() # so that psyco can do its magic
