def munge(n, A, B):
    M = set()
    N = str(n)
    for s in xrange(1, len(N)):
        m = int(N[s:] + N[:s])
        if n < m <= B:
            M.add(m)
    return len(M)

def count(A, B):
    total = 0
    for n in xrange(A, B+1):
        total += munge(n, A, B)
    return total

infile = open("C-large.in", "r")
outfile = open("C-large.out", "w")
T = int(infile.readline())
for casenum in range(1, T+1):
    A, B = map(int, infile.readline().split())
    outfile.write("Case #%d: %d\n" % (casenum, count(A, B)))
