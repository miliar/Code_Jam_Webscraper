def solve(fl):
    tl=[]
    op=[]
    for x in fl:
        tl.append(vd[x])

    op.append(tl[0]+tl[1]+tl[2]+tl[3]) #row1
    op.append(tl[4]+tl[5]+tl[6]+tl[7]) #row2
    op.append(tl[8]+tl[9]+tl[10]+tl[11]) #row3
    op.append(tl[12]+tl[13]+tl[14]+tl[15]) #row4
    op.append(tl[0]+tl[4]+tl[8]+tl[12]) #col1
    op.append(tl[1]+tl[5]+tl[9]+tl[13]) #col2
    op.append(tl[2]+tl[6]+tl[10]+tl[14]) #col3
    op.append(tl[3]+tl[7]+tl[11]+tl[15]) #col4
    op.append(tl[0]+tl[5]+tl[10]+tl[15]) #diag1
    op.append(tl[3]+tl[6]+tl[9]+tl[12]) #diag2

    if (20 in op) or (40 in op):
        return "X won"
    elif (4 in op) or (28 in op):
        return "O won"
    elif 0 in tl:
        return "Game has not completed"
    else:
        return "Draw"


vd = {".":0,"O":1,"X":5,"T":25}

fi = open("A-large.in","r")
fo = open("A-large.out","w")

n = int(fi.readline())

for i in range(1,n+1):
    fl=""
    for j in range(4):
        fl += fi.readline()[:4]
    o= "Case #"+str(i)+": "+solve(fl)
    print o
    fi.readline()
    fo.write(o+"\n")

fo.close()
fi.close()
print "Done!"
