import sys

if __name__ == "__main__":
    infile = open(sys.argv[1])
    outfile = open(sys.argv[2], 'w')
    T = infile.readline()
    T = int(T.strip())
    for case in range(T):
        line = infile.readline()
        C, F, X = map(float, line.strip().split())
        if C >= X:
            res = X / 2.
            print >> outfile, 'Case #%d: %.7f' % (case + 1, res)
            continue
        n = X / C - 2. / F
        if int(n) == n:
            n = int(n) - 1
        else:
            n = int(n)
        res = X / (2 + n * F)
        res += sum([C / (2 + i * F) for i in range(n)])
        print >> outfile, 'Case #%d: %.7f' % (case + 1, res)
    infile.close()
    outfile.close()

