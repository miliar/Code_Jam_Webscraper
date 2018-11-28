def rchch(txt):
    Z=0
    W=0
    X=0
    G=0
    U=0
    O=0
    T=0
    F=0
    S=0
    I=0
    for k in txt:
        if k=='Z':
            Z+=1
        elif k=='W':
            W+=1
        elif k=='X':
            X+=1
        elif k=='G':
            G+=1
        elif k=='U':
            U+=1
        elif k=='O':
            O+=1
        elif k=='T':
            T+=1
        elif k=='F':
            F+=1
        elif k=='S':
            S+=1
        elif k=='I':
            I+=1
    zero=Z
    un=O-W-U-Z
    deux=W
    trois=T-W-G
    quatre=U
    cinq=F-U
    six=X
    sept=S-X
    huit=G
    neuf=I-huit-six-cinq
    return([zero,un,deux,trois,quatre,cinq,six,sept,huit,neuf])
    
def main():
    ifn='A-large.in'
    ofn='output.txt'
    f=open(ifn,'r',encoding='utf-8')
    g=open(ofn,'w')
    nb_val=int(f.readline().strip())
    for k in range(nb_val):
        g.write("Case #%d: " %(k+1))
        txt=f.readline().strip()
        S=rchch(txt)
        g.write("0"*S[0])
        g.write("1"*S[1])
        g.write("2"*S[2])
        g.write("3"*S[3])
        g.write("4"*S[4])
        g.write("5"*S[5])
        g.write("6"*S[6])
        g.write("7"*S[7])
        g.write("8"*S[8])
        g.write("9"*S[9])
        g.write('\n')
    f.close()
    g.close()
    return('Fin')
    