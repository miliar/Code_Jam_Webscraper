import utils

if __name__ == "__main__":
    inputFile = "A-small-attempt1.in"
    outputFile = "outputQ1"
    inputData = utils.createReadFile(inputFile)
    outputData = utils.createWriteFile(outputFile)
    cases = inputData.next()
    cases = cases.replace("\n","")
    print cases
    for index in range(1, int(cases) + 1):
        data = []
        count = 10
        count1 = 0
        for row in inputData:
            rowData = row.replace("\n","")
            rowData = rowData.split(" ")
    #        print rowData
            data.append(rowData)
            count1 += 1
            if count1 == 10:
                break
        print "here", data
        first = int(data[0][0])
        second = int(data[5][0])
        print first, second
        firstCol = data[first]
        secondCol = data[second+5]
        print firstCol, secondCol
        flag = -1

        number = -1
        for num1 in firstCol:
            for num2 in secondCol:
                if num1 == num2 and flag == -1:
                    flag = 0
                    number = num1
                elif num1 == num2 and flag == 0:
                    flag = 1
                    number = "Bad magician!"
        if flag == -1:
            flag = 2
            number = "Volunteer cheated!"
    
        outputString = "Case #" + str(index)+ ": " + number + "\n"
        print outputString
        outputData.write(outputString)
                
            
