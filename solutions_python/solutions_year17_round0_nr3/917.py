import utils

if __name__ == "__main__":
    inputFile = 'inputQ3'
    inputFile = 'C-small-2-attempt0.in'
    inputFile = 'C-large.in'
    #inputFile = "D-small-attempt0.in"
    #inputFile = "C-small-attempt0.in"
    #inputFile = "A-large.in.txt"
    #inputFile = "inputQ3"
    outputFile = "outputQ3"
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
        strs = rowData.split(' ') 
        N = int(strs[0])
        K = int(strs[1])
        array = {}
        large = N
        array[large] = 1
        i = 0
        while i < K:
            selectN = large
                
            NNumber = array[selectN]
            i += NNumber
                
            mi = (selectN-1)/2
            ma = (selectN)/2
            if mi in array:
                array[mi] += NNumber
            else:
                array[mi] = NNumber
        
            if ma in array:
                array[ma] +=NNumber
            else:
                array[ma] = NNumber
            array.pop(selectN, None)
            keys = list(array.keys())
            nn = list(reversed(sorted(keys)))
            large = nn[0] 
        outputString = "Case #" + str(index)+ ": " + str(ma) + " " + str(mi) + "\n"
        print outputString
        outputData.write(outputString)



            
