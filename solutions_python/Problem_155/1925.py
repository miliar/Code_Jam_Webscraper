import utils

if __name__ == "__main__":
    inputFile = "A-small-attempt0.in.txt"
    inputFile = "A-large.in.txt"
    #inputFile = "inputQ1"
    outputFile = "outputQ1"
    inputData = utils.createReadFile(inputFile)
    outputData = utils.createWriteFile(outputFile)
    cases = inputData.next()
    cases = cases.replace("\n","")
    print cases
    for index in range(1, int(cases) + 1):
        print "case ", index
        claped = 0
        friends = 0
        rowData = inputData.next()
        rowData = rowData.replace("\n","")
        rowData = rowData.split(" ")
        maxShy = int(rowData[0])
        shyString = rowData[1]
        for i in range(len(shyString)):
            current = shyString[i]
            if int(current) == 0:
                continue
            #print current 
            print claped, i, friends
            if i > claped:
                newFriends = i - claped
                friends += newFriends
                claped += newFriends
            claped += int(shyString[i])
            print claped, i, friends
    #        print rowData
        outputString = "Case #" + str(index)+ ": " + str(friends) + "\n"
        print outputString
        outputData.write(outputString)
                
            
