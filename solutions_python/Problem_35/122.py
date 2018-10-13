total = 5
rowNum = 3 + 2
colNum = 3 + 2
mat = [[10001,10001,10001,10001,10001],[10001,9,6,3,10001],[10001,5,9,6,10001],[10001,3,5,9,10001],[10001,10001,10001,10001,10001]]

import sys
inFile = open(sys.argv[1],"r")
outFile = open("output2", "w")

# Direction finder
def direction(mat,x,y):
    a = mat[x-1][y]
    b = mat[x][y-1]
    c = mat[x][y+1]
    d = mat[x+1][y]
    e = mat[x][y]
    min = e
    if (e<=a) and (e<=b) and (e<=c) and (e<=d):
        return 5 #Sink
    if (a<e) and (b>=a) and (c>=a) and (d>=a):
        return 1 # North
    if (b<e) and (a>=b) and (c>=b) and (d>=b):
        return 2 # West
    if (c<e) and (a>=c) and (b>=c) and (d>=c):
        return 3 # East 
    return 4 # South

total = int(inFile.readline())
for t in range(total):
    mat = []
    matSize = inFile.readline().split(" ")
    rowNum = int(matSize[0]) + 2
    colNum = int(matSize[1]) + 2
    tempMatArr1=[]
    for t3 in range(colNum):
        tempMatArr1.append(10001)
    mat.append(tempMatArr1)
    for t1 in range(rowNum-2):
        compRow = inFile.readline().split(" ")
        tempMatArr = [10001]
        for t2 in compRow:
            tempMatArr.append(int(t2))
        tempMatArr.append(10001)
        mat.append(tempMatArr)
    mat.append(tempMatArr1)

    # Create friend matrix
    fMat = []
    for i in range(rowNum):
        tempMat=[]
        for j in range(colNum):
            if i==0 or i==(rowNum-1) or j==0 or j==(colNum-1):
                tempMat.append(0)
            else:    
                tempMat.append(direction(mat,i,j))
        fMat.append(tempMat)
  
    # Create result matrix
    rMat = []
    for i in range(rowNum):
        tempMat=[]
        for j in range(colNum):
            tempMat.append("")
        rMat.append(tempMat)

    # Mark the drainage
    startChar = "a"
    tempChar="*"
    for i in range(1,rowNum-1):
        for j in range(1,colNum-1):        
            if(rMat[i][j]==""):
                i1=i
                j1=j
                markArr=[]
                markLen=0
                while(fMat[i1][j1]!=5):
                    rMat[i1][j1]=tempChar
                    markArr.append([i1,j1])
                    markLen=markLen+1
                    if(fMat[i1][j1]==1):
                        i1=i1-1	
                    elif(fMat[i1][j1]==2):
                        j1=j1-1
                    elif(fMat[i1][j1]==3):
                        j1=j1+1
                    else:
                        i1=i1+1
                nChar = rMat[i1][j1]
                if(nChar==""):
                    nChar = startChar
                    startChar = chr(ord(startChar)+1)
                for k in range(markLen):
                    rMat[markArr[k][0]][markArr[k][1]]=nChar
                rMat[i1][j1] = nChar
    
    outFile.write("Case #%d:\n" % (t+1,))
    for i in range(1,rowNum-1):
        rowStr = ""
        for j in range(1,colNum-1):
            rowStr= rowStr + rMat[i][j] + " "
        outFile.write(rowStr.rstrip()+"\n")
    
    
inFile.close()
outFile.close()
