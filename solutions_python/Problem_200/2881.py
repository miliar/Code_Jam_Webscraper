allRows = []
inputFileName = 'in2.txt'
outputFileName = 'out2.txt'
#functions
def readFile():
    with open(inputFileName,'r') as file:
        size = int(file.readline())
        global allRows
        for i in range(size):
            line = file.readline()
            allRows.append(line)

#read
readFile()
outputFile = open(outputFileName, 'w+')

#print('start')

#loop
for row in range(len(allRows)):
    prevIndex = 0
    result = ''
    temp = allRows[row][0]
    length = len(allRows[row].rstrip('\n'))
    # print('row: ' + allRows[row])
    for index in range(1,length):
        # print('index: ' + str(index))
        if int(allRows[row][index]) == int(allRows[row][prevIndex]):
            # print('=')
            temp = temp + allRows[row][index]
        elif int(allRows[row][index]) > int(allRows[row][prevIndex]):
            # print('>')
            result = result + temp
            prevIndex = index
            temp = allRows[row][index]
        elif int(allRows[row][index]) < int(allRows[row][prevIndex]):
            # print('<, printing')
            if prevIndex == 0 and allRows[row][prevIndex] == '1':
                # print('boom ' + str(length))
                result = '9'*(length - 1)
            else:
                result = result + str(int(allRows[row][prevIndex])-1)
                nines = '9'*(length - prevIndex - 1)
                result = result + nines

            outputFile.write('Case #{}: {}\n'.format(row + 1, result))
            break
        # print('result = {}, temp = {}'.format(result,temp))
    else: #end of number
        # print('end, printing')
        result = result + temp
        outputFile.write('Case #{}: {}\n'.format(row + 1, result))


#close
outputFile.close()