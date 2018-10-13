#source="C:\Users\Mani\Desktop\A-small-attempt0.in"
source="C:\Users\Mani\Desktop\A-large.in"
dest="C:\Users\Mani\Desktop\Output.txt"
fin=open(source)
fout=open(dest,'w')
t=fin.readline()
t=int(t)
for i in range(t):
    a=[]
    b=[]
    con=0
    c=" "
    for j in range(4):
        m=fin.readline()
        a.append(list(m))
    for j in range(4):
        if "." in a[j]:
            con=con+1
        b=[a[0][j],a[1][j],a[2][j],a[3][j]]
        
        if 'T' in a[j] and a[j].count("X")==3:
            c="X won"
        elif 'T' in a[j] and a[j].count("O")==3:
            c="O won"
        elif a[j].count("X")==4:
            c="X won"
        elif a[j].count("O")==4:
            c="O won"
        elif 'T' in b and b.count("X")==3:
            c="X won"
        elif 'T' in b and b.count("O")==3:
            c="O won"
        elif b.count("X")==4:
            c="X won"
        elif b.count("O")==4:
            c="O won"
    
    b=[a[0][0],a[1][1],a[2][2],a[3][3]]
    
    if 'T' in b and b.count("X")==3:
        c="X won"
    elif 'T' in b and b.count("O")==3:
        c="O won"
    elif b.count("X")==4:
        c="X won"
    elif b.count("O")==4:
        c="O won"
    b=[a[0][3],a[1][2],a[2][1],a[3][0]]
    
    if 'T' in b and b.count("X")==3:
        c="X won"
    elif 'T' in b and b.count("O")==3:
        c="O won"
    elif b.count("X")==4:
        c="X won"
    elif b.count("O")==4:
        c="O won"

    if c==" " and con==0:
        c="Draw"
    elif c==" " and con>0:
        c="Game has not completed"

    m=fin.readline()


    
    i=str(i+1)
    fout.write("Case #"+i+": "+c+"\n")
fin.close()
fout.close()
