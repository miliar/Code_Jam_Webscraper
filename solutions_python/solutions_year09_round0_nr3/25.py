w = "welcome to code jam"
m = {}

def calc(s, i, j):
    if i == len(w): return 1
    if j == len(s): return 0
    if (i, j) in m: return m[i, j]
    ix = s.find(w[i], j)
    if ix == -1:
        m[i, j] = 0
        return 0
    m[i, j] = calc(s, i + 1, ix + 1) + calc(s, i, ix + 1)
    return m[i, j]

N = input()
for n in xrange(N):
    m = {}
    s = raw_input()
    print "Case #%i: %04i" % (n + 1, calc(s, 0, 0) % 10000)
