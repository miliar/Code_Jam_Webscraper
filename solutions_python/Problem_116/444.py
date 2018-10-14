def count(symbol,array):
    cnt=0
    for i in array:
        if i==symbol:
            cnt+=1
    return cnt

def rowCheck(matrix):
    winr="D"
    for i in range(0,4):
        row=[matrix[i][0],matrix[i][1],matrix[i][2],matrix[i][3]]
        if count("X",row)+count("T",row)==4:
            winr="X"
            return winr
        elif count("O",row)+count("T",row)==4:
            winr="O"
            return winr
    return winr

def colCheck(matrix):
    winr="D"
    for i in range(0,4):
        row=[matrix[0][i],matrix[1][i],matrix[2][i],matrix[3][i]]
        if count("X",row)+count("T",row)==4:
            winr="X"
            return winr
        elif count("O",row)+count("T",row)==4:
            winr="O"
            return winr
    return winr

def diagCheck(matrix):
    winr="D"
    diag1=[matrix[0][0],matrix[1][1],matrix[2][2],matrix[3][3]]
    diag2=[matrix[0][3],matrix[1][2],matrix[2][1],matrix[3][0]]
    if count("X",diag1)+count("T",diag1)==4:
        winr="X"
        return winr
    if count("O",diag1)+count("T",diag1)==4:
        winr="O"
        return winr
    if count("X",diag2)+count("T",diag2)==4:
        winr="X"
        return winr
    if count("O",diag2)+count("T",diag2)==4:
        winr="O"
        return winr
    return winr

def presdot(matrix):
    for i in range(0,4):
        if "." in matrix[i]:
            return True
    return False

fl=open("input.in","r")
out=open("output.out","w")
cases=int(fl.readline())
for i in range(0,cases):
    matrix=[]
    for t in range(0,4):
        st=fl.readline()
        matrix.append(list(st[:len(st)-1]))
    bl=fl.readline()
	
    winr=None
    winr=diagCheck(matrix)
    if((winr=="X") or (winr=="O")):
        #print("winr is",winr,i)
        st="Case #"+str(i+1)+": "+winr+" won\n"
        out.write(st)
        continue
    winr=rowCheck(matrix)
    if((winr=="X") or (winr=="O")):
        #print("winr is",winr,i)
        st="Case #"+str(i+1)+": "+winr+" won\n"
        out.write(st)
        continue
    winr=colCheck(matrix)
    if((winr=="X") or (winr=="O")):
        #print("winr is",winr,i)
        st="Case #"+str(i+1)+": "+winr+" won\n"
        out.write(st)
        continue
    if presdot(matrix):
        #print("Game not complete",i)
        st="Case #"+str(i+1)+": Game has not completed\n"
        out.write(st)
    else:
        #print("Game draw",i)
        st="Case #"+str(i+1)+": Draw\n"
        out.write(st)
fl.close()
out.close()
