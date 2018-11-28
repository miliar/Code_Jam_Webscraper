#inputFileName specifies the mapping from googlerese to english
def readMapping(inputFileName):
    inp = open(inputFileName,"r")
    line = inp.readline()
    gToEMap = {}
    while line:
        googChar = line.strip().split(" ")[0]
        engChar = line.strip().split(" ")[1]
        gToEMap[googChar] = engChar
    return gToEMap


#main translation module. Gets the mapping by calling readMapping
def translate(inputFileName,outputFileName):
    inp = open(inputFileName,"r")
    out = open(outputFileName,"w")
    
    noOfTests = int(inp.readline().strip())
    gToEMap = readMapping("mapping.txt")
    caseNo = 1
    print noOfTests

    while caseNo <= noOfTests:
        line = inp.readline()
        transCharList = []
        for ch in line:
            if ch == " "or ch == "\t" or ch == "\n":
                transCharList.append(ch)
            else:
                transCharList.append(gToEMap[ch])
        transLine = "".join(transCharList)
        print transCharList
        print "Case #"+str(caseNo)+": "+transLine
        out.write("Case #"+str(caseNo)+": "+transLine)
        caseNo += 1

    inp.close()        
    out.close()

translate("input.txt","output.txt")
