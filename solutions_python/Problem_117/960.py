f=open("B-large.in")
n = int(f.readline())
list_t = []
f2 = open("output.txt","w")

for i in range (0,n):
    bol=True
    n2 = f.readline().split(" ")
    rows=int(n2[0])
    cols = int(n2[1])
    matrix=[[0 for j in range(0,cols)] for k in range(0,rows)]
    trans1=[[0 for j in range(0,rows)] for k in range(0,cols)]
    trans2=[[0 for j in range(0,rows)] for k in range(0,cols)]
    change_pt=-1
    for m in range(0,rows):
        line=f.readline()
        line_list = line.split(" ")
        for n in range(0,cols):
            matrix[m][n]=int(line_list[n])
    temp_mat = [[100 for j in range(0,cols)] for k in range(0,rows)]

    for m in range (0,rows):
        maxi = matrix[m][0]
        for n in range(0,cols):
            if matrix[m][n]>maxi:
                maxi=matrix[m][n]
        for n in range(0,cols):
            if temp_mat[m][n]>maxi:
                temp_mat[m][n]=maxi

    for m in range (0,cols):
        for n in range (0,rows):
            trans2[m][n]=temp_mat[n][m]
            trans1[m][n]=matrix[n][m]

    for m in range (0,cols):
        maxi = trans1[m][0]
        for n in range(0,rows):
            if trans1[m][n]>maxi:
                maxi=trans1[m][n]
        for n in range(0,rows):
            if trans2[m][n]>maxi:
                trans2[m][n]=maxi

    for m in range (0,cols):
        if trans1[m]!=trans2[m]:
            bol=False
    if bol==False:
        out = "Case #"+str(i+1)+": "+"NO"+"\n"
    else:
        out = "Case #"+str(i+1)+": "+"YES"+"\n"
    f2.write(out)
f2.close()


