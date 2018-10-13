import math
import threading

f = open("B-small-attempt3.in");
out = open('out.txt','w+')


problems = int(f.readline())

def strArrToInts(arr):
    ints = []
    for i in arr:
        ints.append(str(i))

    return ints

def readProblem():
    dims = f.readline().strip('\n')    
    dims = dims.split(' ')
    idims = (int(dims[0]), int(dims[1]))
    dims = idims
    data = []
    for rows in range(dims[0]):
        data.append( strArrToInts(f.readline().strip('\n').split(' ')) )

    return (dims, data)

def checkData(value, data):
    if len(data) == 0:
        return True
    for num in data:
        if value < num:
            return False        
    return True
        
def checkLeft(data, i, j):
    value = data[i][j]
    data = data[i][:j]
    return checkData(value, data)

def checkRight(data, i, j):
    value = data[i][j]
    data = data[i][j+1:]
    return checkData(value, data)

def checkTop(data, i, j):
    value = data[i][j]
    dat = []
    for row in data[:i]:
        dat.append(row[j])
    return checkData(value, dat)

def checkDown(data, i, j):
    value = data[i][j]
    dat = []
    for row in data[i+1:]:
        dat.append(row[j])
    return checkData(value, dat)


def isValid(data, i, j):
    if checkLeft(data, i, j) and checkRight(data, i, j):
        return True

    if checkTop(data,i,j) and checkDown(data,i,j):
        return True
    
    #print(str(i) + " " + str(j))
    return False

def processProblem( dims, data ):
    if (dims[0] == 1 or dims[1] == 1):
        return True
    
    for i in range(dims[0]):
        for j in range(dims[1]):
            if not isValid(data, i, j):
                return False    
    return True    
     
for i in range(problems):
    (dims, data) = readProblem()
    res = processProblem(dims, data)
    if res == True:
        out.write("Case #" + str(i + 1) + ": YES" + "\n")
    else:
        out.write("Case #" + str(i + 1) + ": NO" + "\n")
    print("Case #" + str(i + 1) + ": " + str(res))
    #if (i+1) == 12:
    #    dkdk
        

out.close();    
f.close();
