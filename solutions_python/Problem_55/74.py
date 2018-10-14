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
                R, k, N = [long(tok) for tok in toks]
                toks = inFile.readline().split()
                gs = [long(tok) for tok in toks]

                pos = 0
                people = 0
                money = 0
                numRuns = 0
                firstGroup = None

                beenFirst, runs, moneys = [False] * N, [0] * N, [0] * N

                while(numRuns < R):
                    if pos == firstGroup or people + gs[pos] > k:
                        money += people
                        people = 0
                        numRuns += 1
                        if not beenFirst[firstGroup]:
                            beenFirst[firstGroup] = True
                            runs[firstGroup] = numRuns
                            moneys[firstGroup] = money
                        else:
                            runInc = numRuns - runs[firstGroup]
                            moneyInc = money - moneys[firstGroup]
                            numRepeats = (R - numRuns) / runInc
                            numRuns += numRepeats * runInc
                            money += numRepeats * moneyInc
                        firstGroup = None
                    else:
                        if firstGroup is None: firstGroup = pos
                        people += gs[pos]
                        pos = (pos + 1) % N

                output = "Case #{0}: {1}\n".format(caseNo+1, money)
                outFile.write(output)

if __name__ == "__main__":
    main()
