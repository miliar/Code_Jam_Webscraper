def checkXStraightx():
    for i in xrange(4):
        sucess = True
        for j in xrange(4):
            if(a[i][j] != "X" and a[i][j] != "T"  ):
                sucess = False
        if(sucess):
            return True
    return False

def checkOStraightx():
    for i in xrange(4):
        sucess = True
        for j in xrange(4):
            if(a[i][j] != "O" and a[i][j] != "T"  ):
                sucess = False
        if(sucess):
            return True
    return False

def checkXStraighty():
    for i in xrange(4):
        sucess = True
        for j in xrange(4):
            if(a[j][i] != "X" and a[j][i] != "T"  ):
                sucess = False
        if(sucess):
            return True
    return False

def checkOStraighty():
    for i in xrange(4):
        sucess = True
        for j in xrange(4):
            if(a[j][i] != "O" and a[j][i] != "T"  ):
                sucess = False
        if(sucess):
            return True
    return False

def checkXDiag1():
    for i in xrange(4):
        if(a[i][i] != "X" and a[i][i] != "T"  ):
                return False
    return True

def checkODiag1():
    for i in xrange(4):
        if(a[i][i] != "O" and a[i][i] != "T"  ):
                return False
    return True

def checkXDiag2():
    for i in xrange(4):
        if(a[i][3-i] != "X" and a[i][3-i] != "T"  ):
                return False
    return True

def checkODiag2():
    for i in xrange(4):
        if(a[i][3-i] != "O" and a[i][3-i] != "T"  ):
                return False
    return True
def checkunfilled():
    for i in xrange(4):
        for j in xrange(4):
            if(a[i][j] == "."):
                return True

T =  int(raw_input())
a = []
for testcase in xrange(T):
    a = []
    for rows in range(4):
        row = raw_input()
        a.append([row[0],row[1],row[2],row[3]])
    if(checkXStraightx() or checkXStraighty() or checkXDiag1()or checkXDiag2()):
           print("Case #"+str(testcase+1)+": X won")
    elif(checkOStraightx()  or checkOStraighty() or checkODiag1() or checkODiag2()):
            print("Case #"+str(testcase+1)+": O won")
    elif(checkunfilled()):
            print("Case #"+str(testcase+1)+": Game has not completed")
    else:
        print("Case #"+str(testcase+1)+": Draw")
    raw_input()
        
