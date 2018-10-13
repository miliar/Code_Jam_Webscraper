filename = "A-small-attempt1.in"
outputfile = "magician_result.txt"

def readrow(f):
    rowNum = int(f.readline())

    for j in range(4):
        line = f.readline()
        if j == (rowNum - 1):
            row = [int(i) for i in line.split(" ")]
    return row

def rowComp(r, s):
    sDict = {i:True for i in s}
    ret = -1
    for i in r:
        if sDict.has_key(i):
            if ret == -1:
                ret = i
            else:
                ret = 0
                break
    return ret
    

fin = open(filename, 'r')
fout = open(outputfile, 'w')

caseNum = int(fin.readline())

for i in range(caseNum):
    case = str(i + 1)
    row1 =  readrow(fin)
    row2 =  readrow(fin)
    ret = rowComp(row1, row2)
    if ret == 0:
        fout.write("case #" + case + ": Bad Magician!\r\n")
    elif ret == -1:
        fout.write("case #" + case + ": Volunteer cheated!\r\n")
    else:
        fout.write("case #" + case + ": " + str(ret) + "\r\n")
