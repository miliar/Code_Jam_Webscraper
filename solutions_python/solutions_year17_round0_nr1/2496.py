import sys

CANT_SOLVE = 'IMPOSSIBLE'
DEBUG = False
import re

def solveCase(happyString, k):
    happyArray = [char == '+' for char in happyString]
    #Greedy:
    nFlips = 0
    for i in range(len(happyArray)):
        if not happyArray[i]:
            #Check flip is OK
            if not (i+k-1 < len(happyArray)):
                return CANT_SOLVE

            else:
                #left Flip
                nFlips = nFlips + 1
                for f in range(k):
                    flipIndex = i+f
                    happyArray[ flipIndex ] = not happyArray[ flipIndex ]
                if DEBUG:
                    print(
                        "Flip num %s to %s" % (
                            nFlips,"".join(
                                ["+" if x else '-' for x in happyArray]
                            )
                        )
                    )
    #End of flipping, just verify that all are ok, as they must be
    for i in range(len(happyArray)):
        if not happyArray[i]:
            raise RuntimeError("Greedy flipping has failed to flip all or "
                               "notify impossibility")
    
    return nFlips


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: pancake.py inputfile outputfile", file=sys.stderr)
        sys.exit()

    with open(sys.argv[1], 'r') as fin:
        nCases = int(fin.readline().strip())

        with open(sys.argv[2], 'w') as fout:
            for caseNumMinusOne in range(nCases):
                line = fin.readline().strip()
                (happyString, kString) = re.split(r'\s+', line)

                print(
                    'Case #%s: %s' % (
                        caseNumMinusOne + 1,
                        solveCase(happyString, int(kString)),
                    ),
                    file = fout,
                )
                



sys.stdin
