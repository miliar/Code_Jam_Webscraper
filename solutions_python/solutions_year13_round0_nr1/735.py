f = open("c:/Users/Laszlo/Documents/Program/Python/CodeJam/2013/A-large.in")
out = open("c:/Users/Laszlo/Documents/Program/Python/CodeJam/2013/test1.out", "w+")

N = int(f.readline())

def check(lines):
    O1= set(['O','T'])
    O2= set(['O'])
    X1= set(['X','T'])
    X2= set(['X'])
    complete = True
    #check horizontal lines first
    for i in xrange(4):
        s = set(lines[i][0:4])
        if s==O1 or s==O2:
            return 'O won'
        elif s==X1 or s==X2:
            return 'X won'
        elif '.' in s:
            complete = False
    #check vertical lines
    for i in xrange(4):
        column =[]
        for j in xrange(4):
            column.append(lines[j][i])
        s = set(column)
        if s==O1 or s==O2:
            return 'O won'
        elif s==X1 or s==X2:
            return 'X won'
        elif '.' in s:
            complete = False
    #check diagonals
    diag=[]
    for i in xrange(4):
        diag.append(lines[i][i])
    s = set(diag)
    if s==O1 or s==O2:
        return 'O won'
    elif s==X1 or s==X2:
        return 'X won'
    elif '.' in s:
        complete = False
    diag=[]
    for i in xrange(4):
        diag.append(lines[3-i][i])
    s = set(diag)
    if s==O1 or s==O2:
        return 'O won'
    elif s==X1 or s==X2:
        return 'X won'
    elif '.' in s:
        complete = False
    if complete:
        return 'Draw'
    else:
        return 'Game has not completed'
    

for i in xrange(N):
    lines=[]
    for j in xrange(4):
        lines.append(f.readline())
    result = check(lines)
    out.write("Case #%d: %s\n" %(i+1, result))
    
    f.readline()
    
    

f.close()
out.close()
