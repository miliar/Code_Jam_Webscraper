T=int(input())
for t in range(T):
    line=input().split()
    N=int(line[0])
    colors={}
    R=int(line[1])

    O=int(line[2])

    Y=int(line[3])

    G=int(line[4])

    B=int(line[5])

    V=int(line[6])

    newR=R-G
    colors["R"]=newR
    newY=Y-V
    colors["Y"]=newY
    newB=B-O
    colors["B"]=newB
    newN=newR+newY+newB
    if R==0 and G==0 and Y==0 and V==0 and newB==0:
        print ("Case #" + str(t+1) + ": " + "BO"*O)
        continue
    if R==0 and G==0 and B==0 and O==0 and newY==0:
        print ("Case #" + str(t+1) + ": " + "YV"*V)
        continue
    if Y==0 and V==0 and B==0 and O==0 and newR==0:
        print ("Case #" + str(t+1) + ": " + "RG"*G)
        continue
    if (newR>newN/2 or newB>newN/2 or newY>newN/2):
        print ("Case #" + str(t+1) + ": IMPOSSIBLE")
    elif (newR<1 and G>0) or (newB<1 and O>0) or (newY<1 and V>0):
        print ("Case #" + str(t+1) + ": IMPOSSIBLE")
    else:
        maxcolor=""
        
        if newR>=newB and newR>=newY:
            maxcolor="R"
            other1="Y"
            other2="B"
        elif newB>=newR and newB>=newY:
            maxcolor="B"
            other1="Y"
            other2="R"
        else:
            maxcolor="Y"
            other1="B"
            other2="R"
        if newN%2==0:
            outstr=""
            while colors[maxcolor]>0:
                outstr+=maxcolor
                colors[maxcolor]-=1
                if colors[other1]>=colors[other2]:
                    outstr+=other1
                    colors[other1]-=1
                else:
                    outstr+=other2
                    colors[other2]-=1
            outstr+=(other1+other2)*colors[other1]
            
        else:
            outstr=maxcolor+other1+other2
            colors[maxcolor]-=1
            colors[other1]-=1
            colors[other2]-=1
            while colors[maxcolor]>0:
                outstr+=maxcolor
                colors[maxcolor]-=1
                if colors[other1]>=colors[other2]:
                    outstr+=other1
                    colors[other1]-=1
                else:
                    outstr+=other2
                    colors[other2]-=1
            outstr+=(other1+other2)*colors[other1]
        if newR>0:
            outstr=outstr[:outstr.index("R")] + "RG"*G + outstr[outstr.index("R"):]
        if newB>0:
            outstr=outstr[:outstr.index("B")] + "BO"*O + outstr[outstr.index("B"):]
        if newY>0:
            outstr=outstr[:outstr.index("Y")] + "YV"*V + outstr[outstr.index("Y"):]
        
        print ("Case #" + str(t+1) + ": " + outstr)

    
