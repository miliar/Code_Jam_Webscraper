IN = 'C-small-attempt0.in'
OUT = 'c.out'

def vxor(X):
    return reduce(lambda a, b: a ^ b, X, 0)

with open(IN, 'r') as fin:
    with open(OUT, 'w') as fout:
        lines = fin.readlines()
        T = int(lines.pop(0))

        for case in xrange(1, T + 1):
            N = int(lines.pop(0))
            C = map(int, lines.pop(0).split())

            best = -1
            for i in xrange(1, (2 ** N) - 1):
                bi = bin(i)[1:]
                pile1 = [C[j] for j in xrange(N) if (i >> j) % 2 == 0]
                pile2 = [C[j] for j in xrange(N) if (i >> j) % 2 == 1]

                if vxor(pile1) == vxor(pile2):
#                    print pile1, pile2
                    bsum = max(sum(pile1), sum(pile2))
                    if bsum > best:
                        best = bsum

            if best == -1:
                print 'Case #%d: NO' % case
                fout.write('Case #%d: NO\n' % case)
            else:
                print 'Case #%d: %d' % (case, best)
                fout.write('Case #%d: %d\n' % (case, best))

            
            
