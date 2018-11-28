def getWon(s):
    for i in range(4):
        if (s[i][0]=="X" or s[i][0]=="T")   and (s[i][1]=="X" or s[i][1]=="T") and (s[i][2]=="X" or s[i][2]=="T") and (s[i][3]=="X" or s[i][3]=="T"):
            return "X won"
        if (s[i][0]=="O" or s[i][0]=="T") and (s[i][1]=="O" or s[i][1]=="T") and (s[i][2]=="O" or s[i][2]=="T") and (s[i][3]=="O" or s[i][3]=="T"): 
            return "O won"
    for i in range(4):
        if (s[0][i]=="X" or s[0][i]=="T") and (s[1][i]=="X" or s[1][i]=="T") and (s[2][i]=="X" or s[2][i]=="T") and (s[3][i]=="X" or s[3][i]=="T"):
            return "X won"
        if (s[0][i]=="O" or s[0][i]=="T") and (s[1][i]=="O" or s[1][i]=="T") and (s[2][i]=="O" or s[2][i]=="T") and (s[3][i]=="O" or s[3][i]=="T"):
            return "O won"
    if (s[0][0]=="X" or s[0][0]=="T") and (s[1][1]=="X" or s[1][1]=="T") and (s[2][2]=="X" or s[2][2]=="T") and (s[3][3]=="X" or s[3][3]=="T"):
            return "X won"
    if (s[0][3]=="X" or s[0][3]=="T") and (s[1][2]=="X" or s[1][2]=="T") and (s[2][1]=="X" or s[2][1]=="T") and (s[3][0]=="X" or s[3][0]=="T"):
            return "X won"
    if (s[0][0]=="O" or s[0][0]=="T") and (s[1][1]=="O" or s[1][1]=="T") and (s[2][2]=="O" or s[2][2]=="T") and (s[3][3]=="O" or s[3][3]=="T"):
            return "O won"
    if (s[0][3]=="O" or s[0][3]=="T") and (s[1][2]=="O" or s[1][2]=="T") and (s[2][1]=="O" or s[2][1]=="T") and (s[3][0]=="O" or s[3][0]=="T"):
            return "O won"

    for i in range(4):
        for j in range(4):
            if s[i][j]==".":
                return "Game has not completed"
    return "Draw"

f=file("my2.txt","r")

lines=f.readlines()
n=int(lines[0])
lines=lines[1:]
lines=[x.replace("\n","") for x in lines if not x=='\n']
res=[]
for i in range(n):
    res.append("Case #"+str(i+1)+": "+getWon(lines[:4]))
    lines=lines[4:]
f.close()
f=file("res.txt","w")
f.write("\n".join(res));
f.close()

