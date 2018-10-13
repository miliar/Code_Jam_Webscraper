def show_output(tab,case):
    hasDot=False
    for i in range(4):
        xR=0
        oR=0
        for j in range(4):
            if tab[i][j]=='.':
                hasDot=True
            if tab[i][j]=='x' or tab[i][j]=='t':
                xR=xR+1
            if tab[i][j]=='o' or tab[i][j]=='t':
                oR=oR+1
        if xR==4 or oR==4:
            break
    if xR!=4 or oR!=4: 
        for i in range(4):
            xC=0
            oC=0
            for j in range(4):
                if tab[j][i]=='x' or tab[j][i]=='t':
                    xC=xC+1
                if tab[j][i]=='o' or tab[j][i]=='t':
                    oC=oC+1
            if xC==4 or oC==4:
                break
    xD1=0
    oD1=0
    xD2=0
    oD2=0
    for k in range(4):
        if tab[k][k]=='x' or tab[k][k]=='t':
            xD1=xD1+1
        if tab[k][k]=='o' or tab[k][k]=='t':
            oD1=oD1+1
        if tab[k][4-k-1]=='x' or tab[k][4-k-1]=='t':
            xD2=xD2+1
        if tab[k][4-k-1]=='o' or tab[k][4-k-1]=='t':
            oD2=oD2+1
    if xR==4 or xC==4 or xD1==4 or xD2==4:
        ans='X won'
    elif oR==4 or oC==4 or oD1==4 or oD2==4:
        ans='O won' 
    elif hasDot:
        ans='Game has not completed'
    else:
        ans='Draw'

    print 'Case #{0}: {1}'.format(case,ans)

f = open('input.txt','r')
n = int(f.readline())
for i in range(n):
    j=0
    table = []
    while j<4:
        tmp = f.readline().strip().lower()
        if len(tmp)==0:
            continue
        table.append(tmp)
        j=j+1
    show_output(table,i+1)

    


