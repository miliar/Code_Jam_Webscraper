import sys

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
            for i in xrange(numCases):
                toks = inFile.readline().split()
                N = long(toks[0])
                K = long(toks[1])
                pval = 2 ** N
                if K % pval == pval - 1:
                    state = "ON"
                else:
                    state = "OFF"
                outFile.write("Case #{0}: {1}\n".format(i+1, state))

if __name__ == "__main__":
    main()
