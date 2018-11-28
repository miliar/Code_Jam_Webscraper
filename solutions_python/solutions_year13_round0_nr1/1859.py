f=file("file.in",'r')
f2=file("a.out","w")
a=(int)(f.readline())
for k in range(a):
    ans="Game has not completed"
    m=[]
    flag=False
    i=0
    for i in range(4):
        m.append(f.readline())
    tmp=True
    for i in range(4):
        if not m[i][i] in ['X','T']:
            tmp=False
        
    if tmp:
        flag=True
        ans="X won"
    tmp=True
    for i in range(4):
        if not m[i][3-i] in ['X','T']:
            tmp=False
    if tmp:
        flag=True
        ans="X won"
    tmp=True
    for j in range(4):
        tmp=True
        for i in range(4):
            if not m[i][j] in ['X','T']:
                tmp=False
        if tmp:
            flag=True
            ans="X won"
        tmp=True
        for i in range(4):
            if not m[j][i] in ['X','T']:
                tmp=False
        if tmp:
            flag=True
            ans="X won"
    tmp=True
    for i in range(4):
        if not m[i][i] in ['O','T']:
            tmp=False
    if tmp:
        flag=True
        ans="O won"
    tmp=True
    for i in range(4):
        if not m[i][3-i] in ['O','T']:
            tmp=False
    if tmp:
        flag=True
        ans="O won"
    for j in range(4):
        tmp=True
        for i in range(4):
            if not m[i][j] in ['O','T']:
                tmp=False
        if tmp:
            flag=True
            ans="O won"
        tmp=True
        for i in range(4):
            if not m[j][i] in ['O','T']:
                tmp=False
        if tmp:
            flag=True
            ans="O won"
    tmp=True
    if not flag:
        for i in m:
            if '.'in i:
                tmp=False
        if tmp:
            ans="Draw"
    f.readline()
    f2.write('Case #'+str(k+1)+': '+ans+'\n')
f2.close()
f.close()
