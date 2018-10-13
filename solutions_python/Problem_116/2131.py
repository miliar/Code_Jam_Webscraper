  

def findWinner(arr):
    XWin = False
    OWin = False
    Space = 0
    for mylist in arr:
        windict = {}
        for chess in mylist:
            b = windict.get(chess, 0)
            windict[chess] = b + 1
        
        XWin = ((windict.get('X', 0) + windict.get('T', 0)) == 4) or XWin
        OWin = ((windict.get('O', 0) + windict.get('T', 0)) == 4) or OWin
        Space = windict.get('.', 0) + Space
        
    return XWin, OWin, Space

def setDict(windict, chess):
    b = windict.get(chess, 0)
    windict[chess] = b + 1
    return windict

def findX1Winner(arr):
    windict = {}
    windict = setDict(windict, arr[0][0])
    windict = setDict(windict, arr[1][1])
    windict = setDict(windict, arr[2][2])
    windict = setDict(windict, arr[3][3])
    XWin = ((windict.get('X', 0) + windict.get('T', 0)) == 4)
    OWin = ((windict.get('O', 0) + windict.get('T', 0)) == 4)
    return XWin, OWin

def findX2Winner(arr):
    windict = {}
    windict = setDict(windict, arr[0][3])
    windict = setDict(windict, arr[1][2])
    windict = setDict(windict, arr[2][1])
    windict = setDict(windict, arr[3][0])
    XWin = ((windict.get('X', 0) + windict.get('T', 0)) == 4)
    OWin = ((windict.get('O', 0) + windict.get('T', 0)) == 4)
    return XWin, OWin


def getCaseResult(instr, num):
    lines = instr.split('\n')[:4]
    #print lines

    harray = []

    for n in lines:
        #print n, list(n)
        harray.append(list(n))

    sarray = [[r[col] for r in harray] for col in range(len(harray[0]))]  
    #print harray, sarray

    XWin = False
    OWin = False
    Draw = False
    Space = 0
    #heng hang
    XWin1, OWin1, Space1 = findWinner(harray)
    
    #shuhang
    XWin2, OWin2, Space2 = findWinner(sarray)

    #xiehang
    XWin3, OWin3 = findX1Winner(harray)
    XWin4, OWin4 = findX2Winner(harray)

    #Finial summary
    #XWin = XWin1 or XWin2 or XWin3
    #OWin = OWin1 or OWin2 or OWin3
    XWin = XWin1 or XWin2 or XWin3 or XWin4 
    OWin = OWin1 or OWin2 or OWin3 or OWin4 

    Draw = (XWin == OWin)
    NotFinished = (Space1 > 0) and Draw

    case_str = 'Case #%d: ' % num

    if NotFinished:
        print case_str + 'Game has not completed'
    else:
        if Draw:
            print case_str + 'Draw'
        elif XWin:
            print case_str + 'X won'
        elif OWin:
            print case_str + 'O won'


all_lines = open('in.txt','r').readlines()
total = int(all_lines[0])
allcases = {}
count = 0
str = ''
for line in (all_lines[1:]+['\n']):
    count = count + 1
    casenum = count / 5
    if (count % 5) > 0:
        str = str + line
    else:
        allcases[casenum] = str
        str = ''
#print allcases

for num, instr in allcases.iteritems():
    getCaseResult(instr, num)