import sys
from fractions import gcd

def iswin(A, B):
    if B > A:
        A, B = B, A
    return iw(A, B)

def iw(A, B):
    q, r = divmod(A, B)
    if q > 1:
        return True
    elif r == 0:
        return False
    else:
        return not iw(B, r)

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
            for caseNo in xrange(1, numCases+1):
                toks = inFile.readline().split()
                A1, A2, B1, B2 = [long(tok) for tok in toks]
                n = 0
                for A in xrange(A1, A2+1):
                    for B in xrange(B1, B2+1):
                        if iswin(A, B):
                            n += 1

                output = 'Case #{0}: {1}\n'.format(caseNo, n)
                outFile.write(output)

if __name__ == "__main__":
    main()
