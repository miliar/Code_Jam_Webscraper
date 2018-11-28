def count(symbol,array):
    cnt=0
    for i in array:
        if i==symbol:
            cnt+=1
    return cnt

def checkDiagonals(matrix):
    winner="D"
    diag1=[matrix[0][0],matrix[1][1],matrix[2][2],matrix[3][3]]
    diag2=[matrix[0][3],matrix[1][2],matrix[2][1],matrix[3][0]]
    if count("X",diag1)+count("T",diag1)==4:
        winner="X"
        return winner
    if count("O",diag1)+count("T",diag1)==4:
        winner="O"
        return winner
    if count("X",diag2)+count("T",diag2)==4:
        winner="X"
        return winner
    if count("O",diag2)+count("T",diag2)==4:
        winner="O"
        return winner
    return winner

def checkRows(matrix):
    winner="D"
    for i in range(0,4):
        row=[matrix[i][0],matrix[i][1],matrix[i][2],matrix[i][3]]
        if count("X",row)+count("T",row)==4:
            winner="X"
            return winner
        elif count("O",row)+count("T",row)==4:
            winner="O"
            return winner
    return winner

def checkColumns(matrix):
    winner="D"
    for i in range(0,4):
        row=[matrix[0][i],matrix[1][i],matrix[2][i],matrix[3][i]]
        if count("X",row)+count("T",row)==4:
            winner="X"
            return winner
        elif count("O",row)+count("T",row)==4:
            winner="O"
            return winner
    return winner

def dotpresent(matrix):
    for i in range(0,4):
        if "." in matrix[i]:
            return True
    return False

fl=open("input.txt","r")
out=open("output.txt","w")
cases=int(fl.readline())
for i in range(0,cases):
    matrix=[]
    for t in range(0,4):
        st=fl.readline()
        matrix.append(list(st[:len(st)-1]))
    bl=fl.readline()
    #for s in range(0,4):
    #    print(matrix[s])
    winner=None
    winner=checkDiagonals(matrix)
    if((winner=="X") or (winner=="O")):
        print("Winner is",winner,i)
        st="Case #"+str(i+1)+": "+winner+" won\n"
        out.write(st)
        continue
    winner=checkRows(matrix)
    if((winner=="X") or (winner=="O")):
        print("Winner is",winner,i)
        st="Case #"+str(i+1)+": "+winner+" won\n"
        out.write(st)
        continue
    winner=checkColumns(matrix)
    if((winner=="X") or (winner=="O")):
        print("Winner is",winner,i)
        st="Case #"+str(i+1)+": "+winner+" won\n"
        out.write(st)
        continue
    if dotpresent(matrix):
        print("Game not complete",i)
        st="Case #"+str(i+1)+": Game has not completed\n"
        out.write(st)
    else:
        print("Game draw",i)
        st="Case #"+str(i+1)+": Draw\n"
        out.write(st)
fl.close()
out.close()
        
