def solve(N):
    numberAsCharlist = list(str(N))
    i = 0
    while i < len(numberAsCharlist) - 1:
        if numberAsCharlist[i] <= numberAsCharlist[i + 1]:
            i += 1
            continue
        digit = int(numberAsCharlist[i])
        numberAsCharlist[i] = str((digit - 1))

        j = i + 1
        while j < len(numberAsCharlist):
            numberAsCharlist[j] = '9'
            j += 1

        i -= 1
        if i < 0:
            i = 0
    numberAsString = "".join(numberAsCharlist)
    return int(numberAsString)


inputFile = open('B-large.in', 'r')
outputFile = open('B-large.out', 'w')

testCase = int(inputFile.readline())
for case in range(1, testCase + 1):
    number = int(inputFile.readline())
    outputFile.write('Case #{}: {}\n'.format(case, solve(number)))

inputFile.close()
outputFile.close()
