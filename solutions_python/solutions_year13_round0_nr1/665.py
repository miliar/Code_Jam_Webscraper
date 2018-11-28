import math

def demo():
    a=open("A.in")
    b=a.readlines()
    outf=open("out.txt","w")
    
    
    for i in range(int(b[0])):
        line = range(4)
        for j in range(4):
            line[j]=list(b[5*i+j+1][:-1])
        
        res=check(line)
                
        print "Case #"+str(i+1)+": "+str(res)
        outf.write("Case #"+str(i+1)+": "+str(res)+"\n")
    outf.close()


def check(case):
    o=0
    x=0
    for i in case:
       o+=OT(i)
       x+=XT(i)
    
    for i in xrange(4):
        o+=OT([case[0][i],case[1][i],case[2][i],case[3][i]])
        x+=XT([case[0][i],case[1][i],case[2][i],case[3][i]])
    
    o+=OT([case[0][0],case[1][1],case[2][2],case[3][3]])
    x+=XT([case[0][0],case[1][1],case[2][2],case[3][3]])

    o+=OT([case[0][3],case[1][2],case[2][1],case[3][0]])
    x+=XT([case[0][3],case[1][2],case[2][1],case[3][0]])

    
    if o>0: 
        return "O won"

    if x>0:
        return "X won"

    if countFS(case)==0:
        return "Draw"

    return "Game has not completed"


def OT(li):
    counter=0
    for i in li:
        if i=="O" or i=="T":
            counter+=1
    return counter==4

def XT(li):
    counter=0
    for i in li:
        if i=="X" or i=="T":
            counter+=1
    return counter==4

def countFS(case):
    counter=0
    for i in case:
        for j in i:
            if j==".":
                counter+=1
    return counter
    


raw_input("Got data?")
demo()