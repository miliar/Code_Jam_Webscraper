import sys

if __name__ == "__main__":
    inputFile = sys.argv[1]
    outputFile = inputFile.split('.')[0] + '.out'
    outputFileStream = open(outputFile,'w')

    with open(inputFile,'r') as inputFileStream:
        numCases = int(inputFileStream.next())
        for k in range(numCases):
            N = int(inputFileStream.next())
            naomiIn = [float(x) for x in inputFileStream.next().split()]
            kenIn = [float(x) for x in inputFileStream.next().split()]

            naomiSorted = sorted(naomiIn)
            kenSorted = sorted(kenIn)
            naomiScore, i = N, 0
            for x in naomiSorted:
                if i >= N:
                    break
                else:
                    remaining = kenSorted[i:]
                    for y in remaining:
                        if y < x:
                            i += 1
                        else:
                            break
                    if i < N:
                        naomiScore -= 1
                        i += 1
            naomiScore2, i = 0, 0
            naomiSorted, kenSorted = naomiSorted[-1::-1], kenSorted[-1::-1]
            for x in naomiSorted:
                if i >= N:
                    break
                else:
                    remaining = kenSorted[i:]
                    for y in remaining:
                        if y > x:
                            i += 1
                        else:
                            break
                    if i < N:
                        naomiScore2 += 1
                        i += 1
            ans = '{} {}'.format(naomiScore2, naomiScore)
            outputString = 'Case #' + str(k+1) + ': ' + ans
            outputFileStream.write(outputString + '\n')
