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
            T = int(inFile.readline())
            for caseNo in xrange(1, T+1):
                N = int(inFile.readline())
                C = [int(tok) for tok in inFile.readline().split()]

                st = 0
                sx = 0
                low = C[0]
                for Ci in C:
                    if Ci < low:
                        low = Ci
                    st += Ci
                    sx ^= Ci

                if sx != 0:
                    out = 'NO'
                else:
                    out = st - low
                
                outFile.write('Case #{0}: {1}\n'.format(caseNo, out))

if __name__ == "__main__":
    main()
