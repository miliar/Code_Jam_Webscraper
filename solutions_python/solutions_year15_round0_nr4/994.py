def Run_Omino():
    f=open('D://D-small-attempt2.in','r')
    line=f.readlines()
    i=1
    F_out=open('D://OutputDsmall2.txt','w')
    while i < len(line):
        S=line[i].split(" ")
        print S
        Result=Omino(int(S[0]),int(S[1]),int(S[2]))
        F_out.write("Case #"+str(i)+": "+str(Result)+ "\n")
        i = i + 1
        print Result 
        
    F_out.close()    

def Omino(X,R,C):
    Winner=""
    if X==1:
        Winner="GABRIEL"
        return Winner
    elif X==2:
        if (R==1 and C==1) or (R==3 and C==1) or (R==1 and C==3) or (R==3 and C==3):
            Winner="RICHARD"
            return Winner
        else:
            Winner="GABRIEL"
            return Winner            
    elif X==3:
        if (R==2 and C==3) or (R==3 and C==2)or (R==3 and C==3) or (R==3 and C==4) or (R==4 and C==3):
            Winner="GABRIEL"
            return Winner
        else:
            Winner="RICHARD"
            return Winner 
    elif X==4:
        if (R==4 and C==3) or (R==3 and C==4) or (R==4 and C==4):
            Winner="GABRIEL"
            return Winner        
        else:
            Winner="RICHARD"
            return Winner         
    
    