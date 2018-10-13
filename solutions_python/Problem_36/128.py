import sys

strData = "welcome to code jam"
strDataLen = len(strData)

file = open(sys.argv[1],"r")
num = int(file.readline())
fout = open("output","w")

for c in range(num):
    matchStr = file.readline()
    matchStrLen = len(matchStr)

    # Creating the matrix
    mat = []
    for i in range(strDataLen):
        fillMat = []
        for j in range(matchStrLen):
            fillMat.append(0)
        mat.append(fillMat)

    #Copy the matrix 
    matNew = mat
    for i in range(strDataLen):
        for j in range(i,matchStrLen-strDataLen+i+1):
            if strData[i]==matchStr[j]:
                if i!=0 and j!=0:
                    for k in range(j):
                        matNew[i][j]=matNew[i][j] + matNew[i-1][k]
                elif i==0:
                    matNew[i][j] = 1

    #Count total and output string
    totalCount = 0
    for j in range(matchStrLen):
        totalCount = totalCount + matNew[strDataLen-1][j]
    writeStr = "Case #%d: %04d\n" % (c+1,totalCount%10000)
    fout.write(writeStr)
    
file.close()
fout.close()