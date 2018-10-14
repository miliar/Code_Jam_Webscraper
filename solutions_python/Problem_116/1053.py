def ReadInput(f):
    """f = file, organizes file data"""
    lines = f.readlines()
    cases = int(lines[0])
    AllBoards=[]
    for n in range(0,(cases)):
        Board=[[lines[5*n+1], lines[5*n+2], lines[5*n+3], lines[5*n+4]]]
        AllBoards+=Board
    return AllBoards

def Judgement(B):
    """B = list of all Boards, finds results for all Boards"""
    Case = 0
    for i in B:
        judgement = ''
        Case += 1
        lines = []
        for e in i:
            lines.append(e[0:4])
        for n in range(0,4):
            vert = ''
            for m in range(0,4):
                vert +=i[m][n]
            lines.append(vert)
        Rdiag = str(i[0][0]+i[1][1]+i[2][2]+i[3][3])
        Ldiag = str(i[0][3]+i[1][2]+i[2][1]+i[3][0])
        lines.append(Rdiag)
        lines.append(Ldiag)
        if ('XXXX' in lines) or ('TXXX' in lines) or ('XTXX' in lines) or ('XXTX' in lines) or ('XXXT' in lines):
            judgement = 'X won'
        elif ('OOOO' in lines) or ('TOOO' in lines) or ('OTOO' in lines) or ('OOTO' in lines) or ('OOOT' in lines):
            judgement = 'O won'
        else:
            markers = ''
            for p in range(0,4):
                for q in range(0,4):
                    markers+= i[p][q]
            if '.' in markers:
                judgement = 'Game has not completed'                         
            else:
                judgement = 'Draw'
        print "Case #"+str(Case)+': '+str(judgement)
                        
f=file("A-large.txt")
B = ReadInput(f)
Judgement(B)
