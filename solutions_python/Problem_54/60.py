
filename = 'B-large'

def gcd(a, b):
    if a > b: a, b = b, a
    while a != 0:
        a, b = b % a, a
    return b

fin = open(filename + '.in')
fout = open(filename + '.out', 'w')
cases = int(fin.readline().strip())
for case in xrange(1, cases + 1):
    t = [int(x) for x in fin.readline().strip().split()]
    n = t.pop(0)
    t.sort()
    s = t[1] - t[0]
    for i in xrange(1, n - 1):
        s = gcd(s, t[i + 1] - t[i])
    ans = t[0] % s
    if ans != 0: ans = s - ans
    fout.write('Case #%d: %d\n' % (case, ans))
fin.close()
fout.close()
