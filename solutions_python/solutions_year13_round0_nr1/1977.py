from sys import argv
f = open(argv[1], "r")

s = int(f.readline())

l = []
li = ['', '', '', '']

xPat = ['XXXX', 'XXXT', 'XXTX', 'XTXX', 'TXXX']
oPat = ['OOOO', 'OOOT', 'OOTO', 'OTOO', 'TOOO']

def processList(x_o):
    diag1 = l[0][0] + l[1][1] + l[2][2] + l[3][3]
    diag2 = l[0][3] + l[1][2] + l[2][1] + l[3][0]
    if x_o == 'X':
        pat = xPat
    else:
        pat = oPat
    for i in pat:
        for j in l:
            if i == j:
                return True
        for j in li:
            if i == j:
                return True
        if i == diag1 or i == diag2:
            return True
    return False

def checkEmpty():
    for s in l:
        if '.' in s:
            return True
    return False
    
for i in range(s):
    for j in range(4):
        l.append(f.readline()[:-1])

    for s in range(4):
        for v in range(4):
            li[s] += l[v][s]

    if processList('X'):
        print "Case #%d: X won" % (i + 1)
    elif processList('O'):
        print "Case #%d: O won" % (i + 1)
    elif checkEmpty():
        print "Case #%d: Game has not completed" % (i + 1)
    else:
        print "Case #%d: Draw" % (i + 1)

    l = []
    li = ['', '', '', '']

    f.readline()
