import fileinput

def solveCase(caseStr, flipSize):
    count = 0
    for i in range(len(caseStr) - flipSize+1):
        if caseStr[i] == False:
            #print "Flipping at",i,"case:"
            #print caseStr
            count += 1
            for j in range(flipSize):
                caseStr[j+i] = not caseStr[i+j]
    if not all(caseStr):
        return "IMPOSSIBLE"
    return str(count)

def main():
    it = fileinput.input()
    it.next()
    for i,l in enumerate(it):
        caseStr,flipSize = l.split()
        flipSize = int(flipSize)
        caseStr = [x == "+" for x in caseStr]
        #print caseStr
        print "Case #%d: %s" % ( i+1, solveCase(caseStr, flipSize))

if __name__ == "__main__":
    main()
