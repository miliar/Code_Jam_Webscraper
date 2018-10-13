import sys

if __name__ == "__main__":
    infile = open(sys.argv[1])
    outfile = open(sys.argv[2], 'w')
    T = infile.readline()
    T = int(T.strip())
    for case in range(T):
        M1, M2 = [], []
        ans1 = int(infile.readline().strip())
        for i in xrange(4):
            line = infile.readline().strip().split()
            M1.append(map(int, line))
        ans2 = int(infile.readline().strip())
        for i in xrange(4):
            line = infile.readline().strip().split()
            M2.append(map(int, line))
        Y = set(M1[ans1 - 1]) & set(M2[ans2 - 1])
        if len(Y) == 1:
            res = str(list(Y)[0])
        elif len(Y) == 0:
            res = 'Volunteer cheated!'
        else:
            res = 'Bad magician!'
        print >> outfile, 'Case #%d: %s' % (case + 1, res)
    infile.close()
    outfile.close()

