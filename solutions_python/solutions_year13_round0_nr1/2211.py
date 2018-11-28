__author__="reszegtivadar"
__date__ ="$Apr 14, 2012 12:49:51 AM$"

if __name__ == "__main__":
    print "Hello";


def computeRes(row0,  row1,  row2,  row3):
    res = ''
    posibilities = ['0r',  '1r',  '2r',  '3r',  '0c',  '1c',  '2c',  '3c','1d',  '2d']
    posibilitiesX = ['0r',  '1r',  '2r',  '3r',  '0c',  '1c',  '2c',  '3c','1d',  '2d']
    posibilitiesO = ['0r',  '1r',  '2r',  '3r',  '0c',  '1c',  '2c',  '3c','1d',  '2d']
    notComplete = []
    
    for i in range(4):
        for j in range(4):
            if vars()["row"+str(i)][j] == '.':
                notComplete.append(str(i)+str(j));
                
            if (vars()["row"+str(i)][j] == 'X' or vars()["row"+str(i)][j] == '.'):
                if str(j)+'c' in posibilitiesO:
                    index = posibilitiesO.index(str(j)+'c')
                    del posibilitiesO[index]
                    
                if str(i)+'r' in posibilitiesO:
                    index = posibilitiesO.index(str(i)+'r')
                    del posibilitiesO[index]

            if (vars()["row"+str(i)][j] == 'O' or vars()["row"+str(i)][j] == '.'):
                if str(j)+'c' in posibilitiesX:
                    index = posibilitiesX.index(str(j)+'c')
                    del posibilitiesX[index]
                    
                if str(i)+'r' in posibilitiesX:
                    index = posibilitiesX.index(str(i)+'r')
                    del posibilitiesX[index]
            
            if (i == j):
                if (vars()["row"+str(i)][j] == 'X' or vars()["row"+str(i)][j] == '.'):
                    if '1d' in posibilitiesO:
                        del posibilitiesO[posibilitiesO.index('1d')]
                if (vars()["row"+str(i)][j] == 'O' or vars()["row"+str(i)][j] == '.'):
                    if '1d' in posibilitiesX:
                        del posibilitiesX[posibilitiesX.index('1d')]
            if (i+j == 3):
                if (vars()["row"+str(i)][j] == 'X' or vars()["row"+str(i)][j] == '.'):
                    if '2d' in posibilitiesO:
                        del posibilitiesO[posibilitiesO.index('2d')]
                if (vars()["row"+str(i)][j] == 'O' or vars()["row"+str(i)][j] == '.'):
                    if '2d' in posibilitiesX:
                        del posibilitiesX[posibilitiesX.index('2d')]
                    
    print "posibeX: ",  posibilitiesX
    print "posibeO: ",  posibilitiesO
    
    
    if (len(posibilitiesX)  == 0 and len(posibilitiesO) > 0):
        if (len(notComplete) > 0):
            for i in range(len(posibilitiesO)):
                if posibilitiesO[i][1] == 'd':
                    if posibilitiesO[i][0] == '1':
                        if ('00' in notComplete or '11' in notComplete or '22' in notComplete or '33' in notComplete ):
                            res = "Game has not completed"
                        else:
                            res = "O won"
                    elif posibilitiesO[i][0] == '2':
                        if ('03' in notComplete or '12' in notComplete or '21' in notComplete or '30' in notComplete ):
                            res = "Game has not completed"
                        else:
                            res = "O won"
                elif posibilitiesO[i][1] == 'r':
                    if (str(posibilitiesO[i][0])+'0' in notComplete or str(posibilitiesO[i][0])+'1' in notComplete or str(posibilitiesO[i][0])+'2' in notComplete or str(posibilitiesO[i][0])+'3' in notComplete):
                        res = "Game has not completed"
                    else:
                        res = "O won"
                elif posibilitiesO[i][1] == 'c':
                    if ('0'+str(posibilitiesO[i][0]) in notComplete or '1'+str(posibilitiesO[i][0]) in notComplete or '2'+str(posibilitiesO[i][0]) in notComplete or '3'+str(posibilitiesO[i][0]) in notComplete):
                        res = "Game has not completed"
                    else:
                        res = "O won"
        else:
            res = "O won"
            
    elif (len(posibilitiesO)  == 0 and len(posibilitiesX) > 0):
        if (len(notComplete) > 0):
            for i in range(len(posibilitiesX)):
                if posibilitiesX[i][1] == 'd':
                    if posibilitiesX[i][0] == '1':
                        if ('00' in notComplete or '11' in notComplete or '22' in notComplete or '33' in notComplete ):
                            res = "Game has not completed"
                        else:
                            res = "X won"
                    elif posibilitiesX[i][0] == '2':
                        if ('03' in notComplete or '12' in notComplete or '21' in notComplete or '30' in notComplete ):
                            res = "Game has not completed"
                        else:
                            res = "X won"
                elif posibilitiesX[i][1] == 'r':
                    if (str(posibilitiesX[i][0])+'0' in notComplete or str(posibilitiesX[i][0])+'1' in notComplete or str(posibilitiesX[i][0])+'2' in notComplete or str(posibilitiesX[i][0])+'3' in notComplete):
                        res = "Game has not completed"
                    else:
                        res = "X won"
                elif posibilitiesX[i][1] == 'c':
                    if ('0'+str(posibilitiesX[i][0]) in notComplete or '1'+str(posibilitiesX[i][0]) in notComplete or '2'+str(posibilitiesX[i][0]) in notComplete or '3'+str(posibilitiesX[i][0]) in notComplete):
                        res = "Game has not completed"
                    else:
                        res = "X won"
        else:
            res = "X won"
            
            
    else:
        if (len(notComplete) > 0):
            res = "Game has not completed"
        else:
            res = "Draw"
            
            
    
        
    return res



from textFile import TextFile
#input = TextFile('compete/A-test.in')
#output = TextFile('compete/A-test.out')

input = TextFile('compete/A-large.in')
output = TextFile('compete/A-large.out')

allLines = input.readLinesFromFile();
print allLines
numberOfLines = int(allLines[0])
print numberOfLines

for i in range(numberOfLines):
    #print allLines[i]
    res = computeRes(allLines[5*i+1],  allLines[5*i+2],  allLines[5*i+3],  allLines[5*i+4])
    
    printedLine = "Case #"+str(i+1)+": "+res+ "\n"
    print (printedLine )
    if (i == 0):
        output.writeToFile(printedLine)
    else:
        output.appendToFile(printedLine)

