'''
Created on 2013-4-14

@author: Martin
'''

'''
Created on 2013-4-14

@author: Martin
'''


def solution(numOfCase, c):
    resDic = {}
    curRow = 1
    for countNum in range(numOfCase):
        mn = c[curRow]
        mn = mn.split()
        m = int(mn[0])
        n = int(mn[1])
        if m*n == m or m*n == n:
            resDic[countNum] = "YES"
            curRow = curRow + m + 1
            continue
        # end if
        curField = [[0 for col in range(n)] for row in range(m)]
        for i in range(m):
            thisRow = c[curRow + i + 1].split()
            for j in range(n):
                curField[i][j] = int(thisRow[j])
            # end for
#        # end for
#        print curField
#        print "##########"
        rowMax = []
        for i in range(m):
            rowMax.append(max(curField[i]))
        colMax = []
        for i in range(n):
            tempMax = 0
            for j in range(m):
                if (curField[j][i] > tempMax):
                    tempMax = curField[j][i]
            colMax.append(tempMax)
            
        isNo = False
        for i in range(m):
            for j in range(n):
                if curField[i][j] < rowMax[i] and curField[i][j] < colMax[j]:
                    isNo = True
                    break
            if isNo:
                break
        if isNo:
            resDic[countNum] = "NO"
        else:
            resDic[countNum] = "YES"
            
        
#        print rowMax
#        print colMax
        
        
        curRow = curRow + m + 1
    # end for
    return resDic
        

if __name__ == "__main__":
    f = open("B-large.in")
    c = f.read()
    c = c.split("\n");
    numOfCase = int(c[0])
    resDic = solution(numOfCase, c)
    for i in resDic:
        resDic[i] = "Case #" + str(i+1) + ": " + resDic[i]
    # print resDic
    f.close()
    g = open("large.out","w")
    for i in resDic:
        if (i == numOfCase-1):
            g.write(resDic[i])
        else:
            g.write(resDic[i] + "\n")
    g.close