def won(arr,char):
    if char == 'X':
        for string in arr:
            if((string == 'XXXT') or (string == 'XXTX') or (string == 'XTXX') or (string == 'TXXX') or (string == 'XXXX')):
                return True
        retVal = False
        for string in arr:
            retVal = True
            if (string[0] != 'X') and (string[0] != 'T'):
                retVal = False
                break
        if retVal:
            return True

        for string in arr:
            retVal = True
            if (string[1] != 'X') and (string[1] != 'T'):
                retVal = False
                break
        if retVal:
            return True

        for string in arr:
            retVal = True
            if (string[2] != 'X') and (string[2] != 'T'):
                retVal = False
                break
        if retVal:
            return True

        for string in arr:
            retVal = True
            if (string[3] != 'X') and (string[3] != 'T'):
                retVal = False
                break
        if retVal:
            return True

        index = 0
        for string in arr:
            retVal = True
            if (string[index] != 'X') and (string[index] != 'T'):
                retVal = False
                break
            index += 1
        if retVal:
            return True

        index = 3
        for string in arr:
            retVal = True
            if (string[index] != 'X') and (string[index] != 'T'):
                retVal = False
                break
            index -= 1
        if retVal:
            return True
        
    elif char == 'O':
        for string in arr:
            if((string == 'OOOT') or (string == 'OOTO') or (string == 'OTOO') or (string == 'TOOO') or (string == 'OOOO')):
                return True

        retVal = False
        for string in arr:
            retVal = True
            if (string[0] != 'O') and (string[0] != 'T'):
                retVal = False
                break
        if retVal:
            return True

        for string in arr:
            retVal = True
            if (string[1] != 'O') and (string[1] != 'T'):
                retVal = False
                break
        if retVal:
            return True

        for string in arr:
            retVal = True
            if (string[2] != 'O') and (string[2] != 'T'):
                retVal = False
                break
        if retVal:
            return True

        for string in arr:
            retVal = True
            if (string[3] != 'O') and (string[3] != 'T'):
                retVal = False
                break
        if retVal:
            return True

        index = 0
        for string in arr:
            retVal = True
            if (string[index] != 'O') and (string[index] != 'T'):
                retVal = False
                break
            index += 1
        if retVal:
            return True

        index = 3
        for string in arr:
            retVal = True
            if (string[index] != 'O') and (string[index] != 'T'):
                retVal = False
                break
            index -= 1
        if retVal:
            return True
    
    return False

def incomplete(arr):
    for string in arr:
        if '.' in string:
            return True
    return False

WORDLIST_INFILENAME = "A-small-attempt1.in"
inFile = open(WORDLIST_INFILENAME, 'r', 0)
WORDLIST_OUTFILENAME = "output.in"
outFile = open(WORDLIST_OUTFILENAME, 'w', 0)
noOfTestCases = inFile.readline()
for iTestCase in range(int(noOfTestCases)):
    arr = []
    for lineNo in range(4):
        line = inFile.readline()
        char = line.strip()
        arr.append(char)
    line = inFile.readline()
    if won(arr,'X'):
        outFile.writelines("Case #"+str(iTestCase+1)+": X won\n")
    elif won(arr,'O'):
        outFile.writelines("Case #"+str(iTestCase+1)+": O won\n")
    elif incomplete(arr):
        outFile.writelines("Case #"+str(iTestCase+1)+": Game has not completed\n")
    else:
        outFile.writelines("Case #"+str(iTestCase+1)+": Draw\n")

inFile.close()
outFile.close()

