#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      rluo
#
# Created:     13/04/2013
# Copyright:   (c) rluo 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def solve(inputfile,outputfile):
    inFile = file(inputfile,'r')
    outFile = open(outputfile,'w')
    totalCases = int(inFile.readline().strip())
    for case in range(totalCases):
        print "Case #%d:"%(case+1),
        format = inFile.readline().strip()
        rows,columns = format.split(" ")
        rows = int(rows)
        columns = int(columns)
##        print "rows=%s,columns=%s"%(rows,columns)
        arr=[]
        maxInARow=[]
        for row in range(rows):
            aLine = inFile.readline().strip()
            arr.append(aLine.split(" "))
##            print
##            print "append %s"%aLine
            maxInARow.append(0)
        maxInAColumn=[]
        for column in range(columns):
            maxInAColumn.append(0)

##        print arr

        for i in range(rows):
            for j in range(columns):
                if int(arr[i][j])>maxInARow[i]:
                    maxInARow[i] = int(arr[i][j])
                if int(arr[i][j])>maxInAColumn[j]:
                    maxInAColumn[j] = int(arr[i][j])

##        print "maxInARow",maxInARow
##        print "maxInAColumn",maxInAColumn

        if check(rows,columns,arr,maxInAColumn,maxInARow):
            print "YES"
        else:
            print "NO"

def check(rows,columns,arr,maxInAColumn,maxInARow):

        for i in range(rows):
            for j in range(columns):
                if int(arr[i][j])>=maxInARow[i] or int(arr[i][j])>=maxInAColumn[j]:
                    pass
                else:
                    return False
        return True




if __name__ == '__main__':
##    inputfile="C:\\dev\\q1\\debug.txt"
    inputfile="C:\\dev\\q1\\B-small-attempt0.in"
    outputfile="C:\\dev\\q1\\B-small-attempt0.out"
    solve(inputfile,outputfile)
