import sys

if __name__ == "__main__":
    inputFile = sys.argv[1]
    outputFile = inputFile.split('.')[0] + '.out'
    outputFileStream = open(outputFile,'w')

    with open(inputFile,'r') as inputFileStream:
        N = int(inputFileStream.next())
        for k in range(N):
            i = int(inputFileStream.next())
            row = []
            col = []
            for count in range(4):
                row.append(inputFileStream.next().split())
            j = int(inputFileStream.next())
            for count in range(4):
                col.append(inputFileStream.next().split())
            ans = list(set(row[i-1]).intersection(set(col[j-1])))
            if not ans:
                ans = 'Volunteer cheated!'
            elif len(ans) > 1:
                ans = 'Bad magician!'
            else:
                ans = ans[0]
            outputString = 'Case #' + str(k+1) + ': ' + ans
            # print outputString
            outputFileStream.write(outputString + '\n')
