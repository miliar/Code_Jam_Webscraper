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
                arr = [int(tok) for tok in inFile.readline().split()]

                count = 0
                for pos, elt in enumerate(arr):
                    if pos+1 != elt:
                        count += 1
                
                outFile.write('Case #{0}: {1:.6f}\n'.format(caseNo, count))

if __name__ == "__main__":
    main()
