# Code Jam 2010
# Round 2
# Problem B

IN = 'E:\\cj\\in\\B.in.txt'
OUT = 'E:\\cj\\out\\b.out'

fin = open(IN, 'r')
fout = open(OUT, 'w')

cases = int(fin.readline())

for case in xrange(1, cases + 1):
    P = int(fin.readline())
    M = map(int, fin.readline().split())
    Q = []
    for p in xrange(P):
        Q.append(map(int, fin.readline().split()))
    # The final counts for everyone.
    # Each semi for half et cetera.

    G = []

    for r in xrange(P+1):
        G.append([0 for x in xrange(2**P)])

    for t in xrange(2**P):
        for r in xrange(1, P + 1):
            which = t/(2**r)
            if r > M[t]:
                G[r][which] = 1

    answer = sum(map(sum, G))

    fout.write('Case #%d: %d\n' % (case, answer))

    
fin.close()
fout.close()
