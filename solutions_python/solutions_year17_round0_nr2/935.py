import utils

if __name__ == "__main__":
    inputFile = 'inputQ2'
    inputFile = 'B-small-attempt1.in'
    inputFile = 'B-large.in'
    #inputFile = "D-small-attempt0.in"
    #inputFile = "C-small-attempt0.in"
    #inputFile = "A-large.in.txt"
    #inputFile = "inputQ3"
    outputFile = "outputQ2"
    inputData = utils.createReadFile(inputFile)
    outputData = utils.createWriteFile(outputFile)
    cases = inputData.next()
    cases = cases.strip()
    print cases
    for index in range(1, int(cases) + 1):
        print "case ", index
        outputString = "Case #" + str(index) + ": "
        
        rowData = inputData.next()
        rowData = rowData.strip()
        strs = list(rowData)
        N = int(rowData)
        print N
        new = []
        for i in range(len(strs)):
            i = len(strs) - i - 1
            if i > 0:
                v = strs[i]
                v1 = strs[i-1]
                if v >= v1:
                    new.append(v)
                else:
                    if i != (len(strs)-1):
                        if strs[i+1] < '9':
                            newLen = len(new)
                            del new[:]
                            for ii in range(newLen):
                                new.append('9')
                    new.append('9')
                    strs[i-1] = chr(ord(v1)-1)
            else:
                v = strs[i]
                if v != '0':
                    new.append(v)
        new = reversed(new)

        n = ''.join(new)

        outputString = "Case #" + str(index)+ ": " + n + "\n"
        print outputString
        outputData.write(outputString)



            
