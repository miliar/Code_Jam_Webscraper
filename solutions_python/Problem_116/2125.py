import os

f=open("A-large.in","r")
r=f.readline()
nb_case = int(r)
r=f.readline()
    
R=open("resultat.txt","w")

for cases in range(nb_case):
    matrix=[[],[],[],[]]
    transposedMatrix=[[],[],[],[]]
    diag1=[]
    diag2=[]
    empty=0
    winO=0
    winX=0
    for i in range(4):
        for j in range(4):
            matrix[i].append(r[j])
            if r[j]=='.':
                empty+=1
        r=f.readline()

    for i in range(4):
        for j in range(4):
            transposedMatrix[i].append(matrix[j][i])

    for i in range(4):
        diag1.append(matrix[i][i])


    for i in range(4):
            diag2.append(matrix[i][3-i])

    for i in range(4):
        if matrix[i].count('O')==4 or (matrix[i].count('O')==3 and matrix[i].count('T')==1):
            winO=1
        if matrix[i].count('X')==4 or (matrix[i].count('X')==3 and matrix[i].count('T')==1):
            winX=1
    for i in range(4):
        if transposedMatrix[i].count('O')==4 or (transposedMatrix[i].count('O')==3 and transposedMatrix[i].count('T')==1):
            winO=1
        if transposedMatrix[i].count('X')==4 or (transposedMatrix[i].count('X')==3 and transposedMatrix[i].count('T')==1):
            winX=1
    for i in range(4):
        if diag1.count('O')==4 or (diag1.count('O')==3 and diag1.count('T')==1):
            winO=1
        if diag1.count('X')==4 or (diag1.count('X')==3 and diag1.count('T')==1):
            winX=1
    for i in range(4):
        if diag2.count('O')==4 or (diag2.count('O')==3 and diag2.count('T')==1):
            winO=1
        if diag2.count('X')==4 or (diag2.count('X')==3 and diag2.count('T')==1):
            winX=1

    if winO==1:
        R.write("Case #"+str(cases+1)+": O won\n")
    elif winX==1:
        R.write("Case #"+str(cases+1)+": X won\n")
    elif winX==0 and winO==0 and empty==0:
        R.write("Case #"+str(cases+1)+": Draw\n")
    else:
        R.write("Case #"+str(cases+1)+": Game has not completed\n")
    r=f.readline()

R.close()


