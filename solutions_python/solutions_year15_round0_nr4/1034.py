import sys

def output(caseNo, name):
    myFile = open("ominoOut4.txt","a")
    myFile.write("Case #%d: %s\n" %(caseNo, name))
    print "Case #%d: %s\n" %(caseNo, name)

def importFile(impFile):
    numCases=int(impFile.readline())
    a=[]
    for i in range(0,numCases):
        a.append(impFile.readline().rstrip().split(" "))
    print a
    return a

def checkWin(x, r, c):
    bSide=0
    sSide=0
    if r>c:
        bSide=r
        sSide=c
    else:
        bSide=c
        sSide=r
    area=bSide*sSide
    print area
    if area==1 and x==1:
        return True
    elif area==2 and (x==1 or x==2):
        return True
    elif area==3 and x==1:
        return True
    elif area==4 and (x==1 or x==2):
        return True
    elif area==6 and (x==1 or x==2 or x==3):
        return True
    elif area==9 and (x==1 or x==3):
        return True
    elif area==8 and (x==1 or x==2):
        return True
    elif area==12:
        return True
    elif area==16 and (x==1 or x==2 or x==4):
        return True
    else: return False


myFile = open("D-small-attempt3.in","r")
a=importFile(myFile)
i=0
while i<len(a):
    x=int(a[i][0])
    r=int(a[i][1])
    c=int(a[i][2])
    case=checkWin(x,r,c)
    if case==True:
        name="GABRIEL"
    else: name="RICHARD"
    ##print name
    print x,r,c
    i=i+1
    output(i,name)
