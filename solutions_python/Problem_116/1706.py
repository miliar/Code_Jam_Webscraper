from math import sqrt

def check(mylist):
    #row
    for row in mylist:
        if row.count("X")==4 or (row.count("X")==3 and row.count("T")==1):
            return "X won"
        elif row.count("O")==4 or (row.count("O")==3 and row.count("T")==1):
            return "O won"
    #col
    for i in xrange(4):
        xcnt=0
        ocnt=0
        tcnt=0
        for j in xrange(4):
            if(mylist[j][i]=='X'):
                xcnt += 1
            elif(mylist[j][i]=='O'):
                ocnt += 1
            elif(mylist[j][i]=='T'):
                tcnt += 1
        if(xcnt==4) or (xcnt==3 and tcnt==1):
            return "X won"
        elif(ocnt==4) or (ocnt==3 and tcnt==1):
            return "O won"

    #dig 1
    tmp = mylist[0][0] + mylist[1][1] + mylist[2][2] + mylist[3][3]
    if tmp.count("X")==4 or (tmp.count("X")==3 and tmp.count("T")==1):
        return "X won"
    elif tmp.count("O")==4 or (tmp.count("O")==3 and tmp.count("T")==1):
        return "O won"

    #dig 2
    tmp = mylist[0][3] + mylist[1][2] + mylist[2][1] + mylist[3][0]
    if tmp.count("X")==4 or (tmp.count("X")==3 and tmp.count("T")==1):
        return "X won"
    elif tmp.count("O")==4 or (tmp.count("O")==3 and tmp.count("T")==1):
        return "O won"

    #check dot
    for row in mylist:
        if row.count(".")>0:
           return "Game has not completed"


    return "Draw"



inp = open("A-large.in", "r")
T = int(inp.readline())
for t in xrange(T):
    mylist = list();
    for i in xrange(4):
        mylist.append(inp.readline().replace("\n", ""));

    print "Case #"+ str(t+1) + ": " + check(mylist)
    inp.readline()


