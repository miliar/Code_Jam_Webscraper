
def calcMinimum(listData):
    standing = 0
    added = 0
    for index, value in enumerate(listData):
        i = int(index)
        v = int(value)
        if i <= standing :
            standing = standing + v
        else:
            added = added + 1
            standing = standing + 1 + v
    return added

def calcOutput():
    lineCounter = 0
    with open('/home/likewise-open/ZOHOCORP/tarun-2215/Downloads/A-large.in') as f:
        for line in f:
            if (lineCounter == 0):
                str(lineCounter)
                n = int(line)
                str(n)
            else:
                strLine = str(line)
                listLine = strLine.split(" ")
                #smax = int(listLine[0])
                listIndex = list(listLine[1].rstrip())
                added = calcMinimum(listIndex)
                print("Case #" + str(lineCounter) + ": " + str(added))
            lineCounter = lineCounter + 1
            
calcOutput()