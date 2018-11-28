def specialCase(omino, row, column):
    if omino == 3 and (row == 1 or column == 1):
        return False
    elif omino == 4:
        if row == 1 or column == 1:
            return False
        elif row == 2 or column == 2:
            return False
        else:
            return True
    else:
        return True

filein = open('ominous.in', 'r')
fileout = open('ominous.out', 'w')

numberOfCases = int(filein.readline())

for case in xrange(0, numberOfCases):
    test = map(int, filein.readline().split())
    area = test[1] * test[2]
    if area % test[0] == 0 and specialCase(test[0], test[1], test[2]):
        fileout.write('Case #' + str(case + 1) + ': ' + str('GABRIEL') + '\n')
    else:
        fileout.write('Case #' + str(case + 1) + ': ' + str('RICHARD') + '\n')