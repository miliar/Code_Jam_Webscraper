def check_raw_col(mat_1):
    X=False
    O=False
    not_game_over=False
    for i in range(0,4):
        r1=mat_1[i][0]
        r2=mat_1[i][1]
        r3=mat_1[i][2]
        r4=mat_1[i][3]
        c1=mat_1[0][i]
        c2=mat_1[1][i]
        c3=mat_1[2][i]
        c4=mat_1[3][i]
        if r1=="." or r2=="." or r3=="." or r4=="." or c1=="." or c2=="." or c3=="." or c4==".":
            not_game_over=True
        if (r1==r2==r3==r4 and r1!=".") or (r1==r2==r3 and r4=="T" and r1!=".") or (r1==r2==r4 and r3=="T" and r2!=".") or (r1==r3==r4 and r2=="T" and r3!=".") or (r2==r3==r4 and r1=="T" and r4!="."):
            if r1!="T":
                
                if r1=="X":
                    X=True
                else:
                    O=True
            else:
                if r2=="X":
                    X=True
                else:
                    O=True
        if (c1==c2==c3==c4 and c1!=".") or (c1==c2==c3 and c4=="T" and c1!=".") or (c1==c2==c4 and c3=="T" and c2!=".") or (c1==c3==c4 and c2=="T" and c3!=".") or (c2==c3==c4 and c1=="T" and c4!="."):
            if c1!="T":
                if c1=="X":
                    X=True
                else:
                    O=True
            else:
                if c2=="X":
                    X=True
                else:
                    O=True
    return(X,O,not_game_over)


def check_dia(mat):
    X=False
    O=False
    r1=mat[0][0]
    r2=mat[1][1]
    r3=mat[2][2]
    r4=mat[3][3]

    c1=mat[0][3]
    c2=mat[3][0]
    c3=mat[1][2]
    c4=mat[2][1]
    
    if (r1==r2==r3==r4 and r1!=".") or (r1==r2==r3 and r4=="T" and r1!=".") or (r1==r2==r4 and r3=="T" and r2!=".") or (r1==r3==r4 and r2=="T" and r3!=".") or (r2==r3==r4 and r1=="T" and r4!="."):
        if r1!="T":
            if r1=="X":
                X=True
            else:
                O=True
        else:
            if r2=="X":
                X=True
            else:
                O=True
    if (c1==c2==c3==c4 and c1!=".") or (c1==c2==c3 and c4=="T" and c1!=".") or (c1==c2==c4 and c3=="T" and c2!=".") or (c1==c3==c4 and c2=="T" and c3!=".") or (c2==c3==c4 and c1=="T" and c4!="."):
        if c1!="T":
            if c1=="X":
                X=True
            else:
                O=True
        else:
            if c2=="X":
                X=True
            else:
                O=True
    return(X,O)



def general():
    file=open("A-large.in","r")
    out=open("google_it.txt","w")
    n=int(file.readline().strip())
    
    for case in range(1,n+1):
        mat=[]
        for i in range(0,4):
            mat+=[file.readline().strip()]

        X,O,not_game=check_raw_col(mat)
        X_dia,O_dia=check_dia(mat)

        X_tot=X or X_dia
        O_tot=O or O_dia

        if X_tot and O_tot:
            out.write("Case #%d: Draw\n" %(case))
        elif X_tot:
            out.write("Case #%d: X won\n" %(case))
        elif O_tot:
            out.write("Case #%d: O won\n" %(case))
        elif not_game:
            out.write("Case #%d: Game has not completed\n" %(case))
        else:
             out.write("Case #%d: Draw\n" %(case))
             
        blank=file.readline().strip()
    file.close()
    out.close() 


general()


