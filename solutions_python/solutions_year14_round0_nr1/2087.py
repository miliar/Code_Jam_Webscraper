import sys

cases = int(sys.stdin.readline())
for case in range(cases):
    firstGuess = int(sys.stdin.readline())
    grid1 = [map(int, sys.stdin.readline().split(' ')) for i in range(4)]
    row1 = grid1[firstGuess - 1]

    secondGuess = int(sys.stdin.readline())
    grid2 = [map(int, sys.stdin.readline().split(' ')) for i in range(4)]
    row2 = grid2[secondGuess - 1]

    s = set(row1) & set(row2)
    if len(s) == 1:
        print "Case #{0}: {1}".format(case + 1, next(iter(s)))
    elif len(s) > 1:
        print "Case #{0}: Bad Magician!".format(case + 1)
    else:
        print "Case #{0}: Volunteer cheated!".format(case + 1)
