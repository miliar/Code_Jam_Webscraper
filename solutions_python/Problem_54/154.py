import sys
from fractions import gcd

def main(argv=None):
    if not argv:
        argv = sys.argv[1:]
    if len(argv) >= 1:
        inFileName= argv[0]
    else:
        inFileName = "test.in"
    if len(argv) >= 2:
        outFileName = argv[1]
    else:
        outFileName = "out.out"

    with open(inFileName) as inFile:
        with open(outFileName, 'w') as outFile:
            numCases = int(inFile.readline())
            for caseNo in xrange(numCases):
                toks = inFile.readline().split()
                N = long(toks[0])
                ts = [long(tok) for tok in toks[1:]]
                ts.sort()
                diffs = []
                for i in xrange(1, len(ts)):
                    diffs.append(ts[i] - ts[i-1])

                T = reduce(gcd, diffs)
                y = (T - (ts[0] % T)) % T

                outFile.write("Case #{0}: {1}\n".format(caseNo+1, y))

if __name__ == "__main__":
    main()
