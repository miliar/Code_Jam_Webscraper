#Tic-tac-toe-tomek

tühiMaatriks=[
[".",".",".","."],
[".",".",".","."],
[".",".",".","."],
[".",".",".","."]
]

def kontroll(m):
    if kR(m,"X") or kV(m,"X") or kVER(m,"X"):
        return "X won"
    elif kR(m,"O")or kV(m,"O")or kVER(m,"O"):
        return "O won"
    else:
        return kDraw(m)

def kDraw(m):
    for i in range(4):
        for j in range(4):
            if m[i][j] == ".":
                return "Game has not completed"
    return "Draw"

def kV(m,x):
    global vastus
    for i in range(4):
        z=0
        for j in range(4):
            if m[j][i] ==x or m[j][i] =="T":
                z+=1
            if z==4:
                return True

def kR(m,x):
    for i in range(4):
        z=0
        for j in range(4):
            if m[i][j] ==x or m[i][j] =="T":
                z+=1
            if z==4:
                return True

def kVER(m,x):
    z=0
    y=0
    for i in range(4):
        if m[i][i] ==x or m[i][i] =="T":
            z+=1
        if m[i][3-i] ==x or m[i][3-i] =="T":
            y+=1
        if y==4 or z==4:
            return True

def main(Input):  
    Input=Input.split("\n")
    maatriks=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    nr=int(Input[0].strip())
    for n in range(nr):
        mat=Input[1+n*5:5+n*5]
        for i in range(4):
            for j in range(4):
                maatriks[i][j]=mat[i][j]
        print("Case #{0}: ".format(str(n+1))+kontroll(maatriks))
        with open("output.txt", "a") as fail2:
            fail2.write(str("Case #{0}: ".format(str(n+1))+kontroll(maatriks)+"\n"))

fail=""
f=open("A-large.in")
for i in f:
    fail+=i
main(fail)
f.close()
