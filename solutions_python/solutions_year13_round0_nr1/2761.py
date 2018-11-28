def output(decision,n):
    outputFile = open("output.txt",'a')
    outputFile.write('Case #'+ str(n) + ': ' + decision + '\n')
    
def decide(ln1,ln2,ln3,ln4,n):
    draw="Draw"
    xWon="X won"
    oWon="O won"
    GmRem="Game has not completed"
    #horizintal
    t=0
    if ln1[t] == 'T':
        t=1
    for i in range(0,5):
        if ln1[t]=='.':
            break
        #print i,ln1[i]
        if i == 4:
            if ln1[t] == "X":
                output(xWon,n)
                #print "Xwon",n
                return
            else:
                output(oWon,n)
                #print "owon",n
                return
        if ln1[i] == 'T':
            continue
        if ln1[i] != ln1[t]:
            break
    t=0
    if ln2[t] == 'T':
        t=1
    for i in range(0,5):
        if ln2[t]=='.':
            break
        #print i,ln2[i]
        if i == 4:
            if ln2[t] == "X":
                output(xWon,n)
                return
                #print "Xwon",n
            else:
                output(oWon,n)
                return
        if ln2[i] == 'T':
            continue
        if ln2[i] != ln2[t]:
            break
    t=0
    if ln3[t] == 'T':
        t=1
    for i in range(0,5):
        if ln3[t]=='.':
            break
        #print i,ln3[i]
        if i == 4:
            if ln3[t] == "X":
                output(xWon,n)
                return
                #print "Xwon",n
            else:
                output(oWon,n)
                return
        if ln3[i] == 'T':
            continue
        if ln3[i] != ln3[t]:
            break
    t=0
    if ln4[t] == 'T':
        t=1
    for i in range(0,5):
        if ln4[t]=='.':
            break
        #print i,ln4[i]
        if i == 4:
            if ln4[t] == "X":
                output(xWon,n)
                return
                #print "Xwon",n
            else:
                output(oWon,n)
                return
        if ln4[i] == 'T':
            continue
        if ln4[i] != ln4[t]:
            break        

    #vertical
    #print "vertical"
    for j in range(0,4):
        t=ln1[j]
        if t == 'T':
            t=ln2[j]
        #print t
        if t =='.':
            continue
        if ln1[j]!=t or ln1[j]=='T':
            continue
        if ln2[j]!=t or ln2[j]=='T':
            continue
        if ln3[j]!=t or ln3[j]=='T':
            continue
        if ln4[j]!=t or ln4[j]=='T':
            continue
        if t == "X":
            output(xWon,n)
            #print "VXwon",n
            return
        else:
            output(oWon,n)
            #print "VOwon",n
            return
    #diagonal
    t=ln1[3]
    if t == 'T':
        t = ln2[2]
    #print t,"@@@"
    if t !='.':
        if ln1[3]==t or ln1[3]=='T':
            if ln2[2]==t or ln2[2]=='T':
                if ln3[1]==t or ln3[1]=='T':
                    if ln4[0]==t or ln4[0]=='T':
                        if t == "X":
                            output(xWon,n)
                            #print "D1Xwon",n
                            return
                        else:
                            output(oWon,n)
                            #print "D1Owon",n
                            return
    t=ln1[0]
    if t == 'T':
        t = ln2[1]
    #print t,"@@@"
    if t !='.':
        if ln1[0]==t or ln1[0]=='T':
            if ln2[1]==t or ln2[1]=='T':
                if ln3[2]==t or ln3[2]=='T':
                    if ln4[3]==t or ln4[3]=='T':
                        if t == "X":
                            output(xWon,n)
                            #print "D2Xwon",n
                            return
                        else:
                            output(oWon,n)
                            #print "D2Owon",n
                            return
   
    
    #Not completed
    if '.' in ln1 or '.' in ln2 or '.' in ln3 or '.' in ln4:
        output(GmRem,n)
        #print "rem",n
        return
    #draw
    output(draw,n)

            
#filename = "A-small-practice.in"
filename = "A-small-attempt0.in"
inputFile = open(filename,'a+r')
if "end" not in inputFile:
    #print "NOOOOOOOOOOOOOOOOOOOOOOOOOOO"
    inputFile.write("end")
inputFile.close()
inputFile = open(filename,'r')
outputFile = open("output.txt",'w')
outputFile.close()
i = 0
n = 0
ln1=[]
ln2=[]
ln3=[]
ln4=[]
for line in inputFile:
    #print i,"@@@@@@@"
    if i == 0:
        i=1
        continue
    elif i%5==1:
        for j in line:
            ln1.append(j)
    elif i%5==2:
        for j in line:
            ln2.append(j)
    elif i%5==3:
        for j in line:
            ln3.append(j)
    elif i%5==4:
        for j in line:
            ln4.append(j)
    elif i%5==0 or line == "end":
        n+=1
        #print n,"!!!!!!"
        decide(ln1,ln2,ln3,ln4,n)
        #print ln1
        #print ln2
##        print ln3
##        print ln4,n
        ln1=[]
        ln2=[]
        ln3=[]  
        ln4=[]
        
    i=i+1
inputFile.close()
            
            

inputFile.close()
