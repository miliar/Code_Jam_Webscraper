import sys

ifs = file("input.txt")
ofs = file("output.txt", "w")

def ReadInts(input = ifs):
  return list(map(int, input.readline().strip().split(" ")))

def GetMatrix(rows, cols, value=0):
    return [[value for i in range(rows)] for j in range(cols)]

def getOne(row):
    ret = 0
    length = len(row)
    for i in row[::-1]:
        if i == 1:
            return length - ret-1
        else:
            ret += 1
    return -1

def dolist(templist):
    length = len(templist)
    if length == 0:
        return []
    if length == 1:
        return [templist[0][1]]
    a = templist[-1][0]
    preNo = length - a + 1
    pre = dolist(templist[:(length-preNo)])
    afterlist = templist[length-preNo:]
    afterlist = [j for i,j in afterlist]
    afterlist.sort()
    return pre + afterlist

caseNo = ReadInts()[0]

for case in range(1, caseNo+1):        
    rowNo = ReadInts()[0]
    matrix = []
    for _ in range(rowNo):
        matrix.append(list(map(int, ifs.readline().strip())))
    templist = []
    for _ in range(rowNo):
        row = matrix[_]
        templist.append((getOne(row), _))

    count = 0
    for i in range(rowNo-1):
        if templist[i][0] > i:
            for j in range(i+1, rowNo):
                if templist[j][0] <= i:
                    break
            templist = templist[:i] + [templist[j]] + templist[i:j]+templist[j+1:]
            count += j-i

    print >> ofs, "Case #%d:" % case, count

    



ifs.close()
ofs.close()



