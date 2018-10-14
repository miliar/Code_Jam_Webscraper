f=open("A-large.in")
out=open("output2.txt",'w')
def inp():
    for i in f:
        return i
def tictac(squ,j):
    count=0
    for i in squ:
        if 'T' in i:
            if i.count('X')==3 or i.count('O')==3:
                if i.count('X')==3:
                    #print "X won"
                    out.write("Case #"+str(j+1)+(": ")+"X won\n")
                else:
                    out.write("Case #"+str(j+1)+(": ")+"O won\n")
                return
        elif i.count('X')==4 or i.count('O')==4:
            if i.count('X')==4:
                out.write("Case #"+str(j+1)+(": ")+"X won\n")
            else:
                out.write("Case #"+str(j+1)+(": ")+"O won\n")
                #print "O won"
            return
            
    for i in squ:
        if '.' in i:
            out.write("Case #"+str(j+1)+(": ")+"Game has not completed\n")
            #print "Game has not completed"
            return
    out.write("Case #"+str(j+1)+(": ")+"Draw\n")
    #print "Draw"

t=int(inp())
for i in range(t):
    squ=[]
    for j in range(4):
        squ.append(inp())
    for j in range(4):
        squ.append(squ[0][j]+squ[1][j]+squ[2][j]+squ[3][j])
    squ.append(squ[0][0]+squ[1][1]+squ[2][2]+squ[3][3])
    squ.append(squ[0][3]+squ[1][2]+squ[2][1]+squ[3][0])
    tictac(squ,i)
    inp()
f.close()
out.close()

    
        
