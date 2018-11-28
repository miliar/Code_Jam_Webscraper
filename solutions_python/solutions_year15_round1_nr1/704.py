
outFile = open('C:/CodeJam/mushrooms_large.txt', 'w')

with open('C:/CodeJam/mushrooms_largeIn.txt', 'r') as inFile:
    tCases = int(inFile.readline())
    case = 1

    while tCases > 0:
        intervals = int(inFile.readline())
        plates = inFile.readline()
        plates = plates.split()

        msms = [int(i) for i in plates]

        mOne = 0
        x = 1
        #methond one for number of eaten mushrooms
        while x < intervals:
            if msms[x-1] <= msms[x]:
                x = x+1
            else:
                mOne = mOne + (msms[x-1]-msms[x])
                x = x+1

        mTwo = 0
        #method two

        y = 1
        rate = 0
        #find the rate
        while y < intervals:
            if (msms[y-1]-msms[y]) >= rate:
                rate = msms[y-1]-msms[y]
                y = y + 1
            else:
                y = y + 1

        z = 1
        #apply the rate
        while z < intervals:
                if msms[z-1] >= rate:
                    mTwo = mTwo + rate
                    z = z + 1

                else:
                    mTwo = mTwo + msms[z-1]
                    z = z + 1

        outFile.write('Case #' + str(case) + ': ' + str(mOne) + ' ' + str(mTwo) + '\n')

        tCases = tCases - 1
        case = case + 1

outFile.close()