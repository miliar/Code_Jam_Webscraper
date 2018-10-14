import sys

t = int(sys.stdin.readline().strip())

for i in xrange(t):
    print "Case #%d:" % (i + 1),

    N, R, O, Y, G, B, V = [int(p) for p in sys.stdin.readline().strip().split()]

    if max(R, Y, B) * 2 > N:
        print "IMPOSSIBLE"
    else:
        let = ['R', 'O', 'Y', 'G', 'B', 'V']
        app = [R, O, Y, G, B, V]

        for jj in xrange(5):
            for kk in xrange(jj + 1, 6):
                if app[jj] < app[kk]:
                    pp = app[jj]
                    app[jj] = app[kk]
                    app[kk] = pp
                    pp = let[jj]
                    let[jj] = let[kk]
                    let[kk] = pp

        last_index = None

        sol = []
        for p in xrange(N):
            m = None        
            for j in range(6):
                if last_index == j:
                    continue
                if (m is None) or (app[j] > app[m]):
                    m = j

            last_index = m
            sol.append(let[m])
            app[m] -= 1

        print "".join(sol)

