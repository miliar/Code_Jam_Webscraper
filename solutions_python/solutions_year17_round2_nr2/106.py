from math import ceil

def solveProblem(N,R,O,Y,G,B,V):
    if O==0 and Y==0 and V==0 and B==0:
        if R==G:
            return "RG"*R
        else:return "IMPOSSIBLE"
    if O==0 and R==0 and G==0 and B==0:
        if Y==V:
            return "VY"*Y
        else: return "IMPOSSIBLE"
    if Y==0 and G==0 and V==0 and R==0:
        if O==B:
            return "OB"*O
        else: return "IMPOSSIBLE"

    red= R-G
    yellow = Y-V
    blue = B-O
    if R!=0 and red<=0: return "IMPOSSIBLE"
    if red <0: return "IMPOSSIBLE"
    if Y!=0 and yellow<=0: return "IMPOSSIBLE"
    if yellow<0: return "IMPOSSIBLE"
    if B!=0 and blue<=0: return "IMPOSSIBLE"
    if blue<0: return "IMPOSSIBLE"

    tmp="R"*red+"Y"*yellow+"B"*blue
    beans=red+yellow+blue
    if yellow*2==beans and blue*2!=beans:
        tmp= "Y"*yellow+"B"*blue+"R"*red
    if yellow*2==beans and red*2!=beans:
        tmp= "Y"*yellow+"R"*red+"B"*blue

    if red*2>beans or yellow*2>beans or blue*2>beans: return "IMPOSSIBLE"

    sol1=list("0"*beans)
    for i in range(ceil(beans/2)):
        sol1[i*2]=tmp[i]
    for i in range(ceil(beans/2),beans):
        sol1[1+2*(i-ceil(beans/2))]=tmp[i]
    sol1="".join(sol1)
    sol1=sol1.replace("R","R"+"GR"*G,1)
    sol1=sol1.replace("Y","Y"+"VY"*V,1)
    sol1=sol1.replace("B","B"+"OB"*O,1)
    return sol1
T=int(input())

for case in range(T):
    line=input().split()
    [N,R,O,Y,G,B,V]=[int(s) for s in line]

    print("Case #"+str(case+1)+": "+solveProblem(N,R,O,Y,G,B,V))
