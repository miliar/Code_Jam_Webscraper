f=open("A-large.in","r")
w=open("sol.in","w")
n=f.readline()
x=1
g=[0,0,0,0]
game=[0,0,0,0]


def checkrows(game=[]):
    xwin=0
    owin=0
    for i in range(0,4):
        for o in range(0,4):
            if str(game[i][o])=="X":
                xwin=xwin+1
            elif str(game[i][o])=="O":
                owin=owin+1
            elif str(game[i][o])=="T":
                xwin=xwin+1
                owin=owin+1
        if xwin==4:
            return 1
        elif owin==4:
            return 2
        xwin=0
        owin=0
    return 3

def checkcol(game=[]):
    xwin=0
    owin=0
    for i in range(0,4):
        for o in range(0,4):
            if str(game[o][i])=="X":
                xwin=xwin+1
            elif str(game[o][i])=="O":
                owin=owin+1
            elif str(game[o][i])=="T":
                xwin=xwin+1
                owin=owin+1
        if xwin==4:
            return 4
        elif owin==4:
            return 5
        xwin=0
        owin=0
    return 6

def checkdiagl(game=[]):
    xwin=0
    owin=0
    for i in range(0,4):
        if str(game[i][i])=="X":
            xwin=xwin+1
        elif str(game[i][i])=="O":
            owin=owin+1
        elif str(game[i][i])=="T":
            owin=owin+1
            xwin=xwin+1
    if xwin==4:
        return 7
    elif owin==4:
        return 8
    else:
        return 9

def checkdiagr(game=[]):
    xwin=0
    owin=0
    for i in range(0,4):
        if str(game[i][int(3-i)])=="X":
            xwin=xwin+1
        elif str(game[i][int(3-i)])=="O":
            owin=owin+1
        elif str(game[i][int(3-i)])=="T":
            owin=owin+1
            xwin=xwin+1
    if xwin==4:
        return 10
    elif owin==4:
        return 11
    else:
        return 12
        

def checkon(game=[]):
    on=False
    for i in range(0,4):
        for o in range(0,4):
            if str(game[i][o])==".":
                on=True
        if on==True:
            return 13
    return 14
                

while x<int(n)+1:
    for i in range(0,4):
        h=f.readline()
        g=[0,0,0,0]
        if len(h)>0:
            for o in range(0,4):
                g[o]=h[o]
            game[i]=g
    a=checkrows(game)
    if a==1:
        w.write("Case #%d: X won\n" %(x))
    elif a==2:
        w.write("Case #%d: O won\n" %(x))
    elif a==3:
        a=checkcol(game)
    if a==4:
        w.write("Case #%d: X won\n" %(x))
    elif a==5:
        w.write("Case #%d: O won\n" %(x))
    elif a==6:
        a=checkdiagl(game)
    if a==7:
        w.write("Case #%d: X won\n" %(x))
    elif a==8:
        w.write("Case #%d: O won\n" %(x))
    elif a==9:
        a=checkdiagr(game)
    if a==10:
        w.write("Case #%d: X won\n" %(x))
    elif a==11:
        w.write("Case #%d: O won\n" %(x))
    elif a==12:
        a=checkon(game)
    if a==13:
        w.write("Case #%d: Game has not completed\n" %(x))
    elif a==14:
        w.write("Case #%d: Draw\n" %(x))
    
    x=x+1
    h=f.readline()
f.close()
w.close()



