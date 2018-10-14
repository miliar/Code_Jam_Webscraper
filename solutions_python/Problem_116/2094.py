def checkrow(string):
    x=string.count("X")
    y=string.count("O")
    t=string.count("T")
    if x+t==4:
        return ("X")
    elif y+t==4:
        return ("O")
    else:
        return ("F")
           
def solve(l):
    pcount=0
    for row in l:
        pcount=pcount+row.count(".")
        re=checkrow(row)
        if re!="F":
            return re+" won"
    strin=""
    for i in range(4):
        strin=l[0][i]+l[1][i]+l[2][i]+l[3][i]
        re=checkrow(strin)
        if re!="F":
            return re+" won"
    dia=l[0][0]+l[1][1]+l[2][2]+l[3][3]
    re=checkrow(dia)
    if re!="F":
        return re+" won"
    dia2=l[0][3]+l[1][2]+l[2][1]+l[3][0]
    re=checkrow(dia2)
    if re!="F":
        return re+" won"
    if pcount==0:
        return "Draw"
    else:
        return "Game has not completed"
f=open("A-large.in","r")
f1=open("output_large.txt","w")
r=f.readlines()
r=r[1:]
l=len(r)
case=1
for i in range(0,l,5):
    result=solve(r[i:i+4])
    resu="Case #"+str(case)+": "+result+"\n"
    f1.write(resu)
    case=case+1
