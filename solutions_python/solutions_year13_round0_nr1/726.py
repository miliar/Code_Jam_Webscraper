f = open("inputalarge.txt")

board = []

cases = int(f.readline())

for c in range(0,cases):
    completed = True
    out = ""
    boardx = []
    boardo = []
    for i in range(0,4):
        l = f.readline()[:4]
        boardx.append(l.replace('T','X'))
        boardo.append(l.replace('T','O'))
        if "." in l:
            completed = False
    
    f.readline()
    for i in boardx:
        if i == "OOOO":
            out = "Case #"+str(c+1)+": O won"
        if i == "XXXX":
            out = "Case #"+str(c+1)+": X won"
    for i in boardo:
        if i == "OOOO":
            out = "Case #"+str(c+1)+": O won"
        if i == "XXXX":
            out = "Case #"+str(c+1)+": X won"
    for i in range(0,4):
        b = ''
        for j in range(0,4):
            b += boardx[j][i]
        if b == "OOOO":
            out = "Case #"+str(c+1)+": O won"
        if b == "XXXX":
            out = "Case #"+str(c+1)+": X won"
    for i in range(0,4):
        b = ''
        for j in range(0,4):
            b += boardo[j][i]
        if b == "OOOO":
            out = "Case #"+str(c+1)+": O won"
        if b == "XXXX":
            out = "Case #"+str(c+1)+": X won"
    if boardx[0][0]+boardx[1][1]+boardx[2][2]+boardx[3][3]=="XXXX":
        out = "Case #"+str(c+1)+": X won"
    if boardx[0][0]+boardx[1][1]+boardx[2][2]+boardx[3][3]=="OOOO":
        out = "Case #"+str(c+1)+": O won"
    if boardo[0][0]+boardo[1][1]+boardo[2][2]+boardo[3][3]=="XXXX":
        out = "Case #"+str(c+1)+": X won"
    if boardo[0][0]+boardo[1][1]+boardo[2][2]+boardo[3][3]=="OOOO":
        out = "Case #"+str(c+1)+": O won"
    if boardx[0][3]+boardx[1][2]+boardx[2][1]+boardx[3][0]=="XXXX":
        out = "Case #"+str(c+1)+": X won"
    if boardx[0][3]+boardx[1][2]+boardx[2][1]+boardx[3][0]=="OOOO":
        out = "Case #"+str(c+1)+": O won"
    if boardo[0][3]+boardo[1][2]+boardo[2][1]+boardo[3][0]=="XXXX":
        out = "Case #"+str(c+1)+": X won"
    if boardo[0][3]+boardo[1][2]+boardo[2][1]+boardo[3][0]=="OOOO":
        out = "Case #"+str(c+1)+": O won"

    if out=="":
        if completed:
            out = "Case #"+str(c+1)+": Draw"
        else:
            out = "Case #"+str(c+1)+": Game has not completed"
    print out
