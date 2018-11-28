from sys import stdin, stdout

stdin = open('A-large.in', 'r')
stdout = open('A-large.out', 'w')

def f(d, n):
    return n*d + d*(1-d)//2 

T = int(stdin.readline().strip())

for t in range(T):
    (n, m) = [int(x) for x in stdin.readline().strip().split()]
    ogn = 0
    opt = 0
    a = []
    for mi in range(m):
        (o, e, p) = [int(x) for x in stdin.readline().strip().split()]
        ogn += f(e-o, n) * p
        a.append((o, e, p))
    a.sort()

    xin = {}
    xout = {}

    for tp in a:
        xin[tp[0]] = xin.get(tp[0], 0) + tp[2]
        xout[tp[1]] = xout.get(tp[1], 0) + tp[2]

    xin = sorted([[key, xin[key]] for key in xin], reverse=True)
    xout = sorted([(key, xout[key]) for key in xout])

    for (e, p) in xout:
        for ls in xin:
            if ls[1] > 0 and ls[0] <= e:
                pp = min(p, ls[1])
                ls[1] -= pp
                p -= pp
                opt += pp * f(e-ls[0], n)
            if p == 0:
                break

    stdout.write('Case #%d: %d\n' % (t+1, (ogn-opt) % 1000002013))
            


stdin.close()
stdout.close()
