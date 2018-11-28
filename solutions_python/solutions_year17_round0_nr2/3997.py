import sys

inputFile = open('B-large.in')
outputFile = open('output.txt', 'w')
numberOfCases = inputFile.readline()

def reverse(num):
      return list(num)[::-1]

for case in range(1, int(numberOfCases)+1):
    reversedInt = reverse(inputFile.readline().rstrip())

    intLength = len(reversedInt)

    for i in range(0, intLength-1):        
        if(reversedInt[i] < reversedInt[i+1]):
            for j in range(0, i+1):        
                reversedInt[j] = '9'
            reversedInt[i+1] = str(int(reversedInt[i+1])-1)

    tidy = ''.join(reverse(reversedInt)).lstrip('0');
        
    outputFile.write('Case #' + str(case) + ': ' + str(tidy) + '\n')

inputFile.close()
outputFile.close()
