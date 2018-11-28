import sys

fin  = sys.stdin
##fin  = file(r'C-small-attempt0.in')
fout = sys.stdout
##fout = file(r'C-small-attempt0.out', 'w')

def main():
    T = int(fin.readline())
    for t in xrange(T):
        ln = fin.readline()
        r, k, n = map(int, ln.split(' '))
        ln = fin.readline()
        g = map(int, ln.split(' '))

        profit = 0
        for i in xrange(r):
            crowd = 0
            riders = []
            while crowd < k:
                try:
                    if g[0] + crowd <= k:
                        crowd += g[0]
                        riders.append(g.pop(0))
                    else:
                        break
                except IndexError:
                    break
            profit += crowd
            g += riders

        fout.write('Case #%d: %s\n' % (t +1, profit))

main()
