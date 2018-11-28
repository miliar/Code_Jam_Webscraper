fin = open('E:\\cj\\B-large.in', 'r')
lines = fin.readlines()
fin.close()

fout = open('E:\\cj\\b.out', 'w')

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

case = 0
cases = int(lines[0])
lp = 1
for case in xrange(1, cases + 1):
    l = lines[lp]
    X = [int(x) for x in l.split()]
    N = X[0]
    t = X[1:]

    gisa = abs(t[0] - t[1])

    for i in xrange(0, N):
        for j in xrange(i + 1, N):
            diff = abs(t[i] - t[j])
            gisa = gcd(max(gisa, diff), min(gisa, diff))

    fout.write('Case #%d: %s\n' % (case, (gisa - (t[0] % gisa))%gisa))
    lp += 1

fout.close()
    
