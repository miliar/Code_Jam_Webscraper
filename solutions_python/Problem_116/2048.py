
lauta = []

def check(nc):
    for i in range(4): 
        if(tarkistaRivi(i)):
            return
        if(tarkistaSarake(i)):
            return
    if (tarkistaDiag()):
        return
    if (nc):
        out.write("Game has not completed\n");
    else:
        out.write("Draw\n")

def tarkistaSarake(a):
    o=x=t=0;
    for i in range(4):
        if(lauta[a][i] == 'X'): x += 1;
        if(lauta[a][i] == 'O'): o += 1;
        if(lauta[a][i] == '.'): t += 1;
    if (t==0 and (x==0 or o==0)):
        if (x==0):
            out.write("O won\n");
        else:
            out.write("X won\n");
        return True;
    return False;

def tarkistaRivi(a):
    o=x=t=0;
    for i in range(4):
        if(lauta[i][a] == 'X'): x += 1
        if(lauta[i][a] == 'O'): o += 1
        if(lauta[i][a] == '.'): t += 1
    if (t==0 and (x==0 or o==0)):
        if (x==0):
            out.write("O won\n")
        else:
            out.write("X won\n")
        return True
    return False;

def tarkistaDiag():
    o=t=x=0;
    for i in range(4):
        if(lauta[i][i] == 'X'): x += 1;
        if(lauta[i][i] == 'O'): o += 1;
        if(lauta[i][i] == '.'): t += 1;
    if (t==0 and (x==0 or o==0)):
        if (x==0):
            out.write("O won\n");
        else:
            out.write("X won\n")
        return True;
    o=t=x=0;
    for i in range(4):
        if(lauta[3-i][i] == 'X'): x += 1;
        if(lauta[3-i][i] == 'O'): o += 1;
        if(lauta[3-i][i] == '.'): t += 1;
    if (t==0 and (x==0 or o==0)):
        if (x==0):
            out.write("O won\n");
        else:
            out.write("X won\n")
        return True
    return False

fin = open("a.in","r")
out=open("a.out","w")
games= int(fin.next())

for j in range(games):
    lauta = []
    nc = False;
    for i in range(4):
        lauta += [fin.next()]
        if ("." in lauta[i]):
            nc = True
    out.write("Case #{0}: ".format(j+1));
    check(nc);
    if j<games-1:
        fin.next()

out.close()
fin.close()
