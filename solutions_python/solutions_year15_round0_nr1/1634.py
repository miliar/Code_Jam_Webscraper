__author__ = 'matteo'

def solveString(stringa):
    print(stringa)
    count = 0
    s = 0
    for index in range(0, len(stringa)):
        if(index <= s):
            s += int(stringa[index])
        else:
            count += (index - s)
            s += int(stringa[index]) + (index - s)
    return count


def solve(a):
    result = []
    for i in a:
        str = i.split(' ')
        result.append(solveString(str[1][:-1]))
    return result

inputFileName = input("nome file:\n")
fileInput = open(inputFileName, mode='r')
n = int(fileInput.readline())
array = []
for i in range(1,n+1):
    line = fileInput.readline()
    array.append(line)
fileInput.close()
solution = solve(array)
outputFileName = inputFileName + 'Out'
fileOutput = open(outputFileName, mode='w')
count = 1
for i in solution:
    fileOutput.write('Case #' + str(count) + ': ' + str(i) + '\n')
    count += 1
fileOutput.close()

