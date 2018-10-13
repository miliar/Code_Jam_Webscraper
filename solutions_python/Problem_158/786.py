cases=int(input())
out=[];
for i in range (0,cases):
    line=str(input())
    line=line.split()
    line=list(map(int,line))#for convert string list to int list
    X=line[0]
    R=line[1]
    C=line[2]
    if (X==1):
        out.append("GABRIEL")
    elif((C*R)%X)!=0:
        out.append("RICHARD")
    elif (X==2):
        if(R*C)<2:
           out.append("RICHARD")
        else:
            out.append("GABRIEL")
    elif (X==3):
            if(X>=R*C):
                out.append("RICHARD")   
            else:
                out.append("GABRIEL")
    elif(X==4):
        if(R*C==16 or R*C==12):
            out.append("GABRIEL")
        else:
            out.append("RICHARD") 
            
    
        
        
            
   





out.reverse()
lenprint=0
while len(out):
    lenprint+=1
    print("Case #",end="")
    print(lenprint,end="")
    print(": ",end="")
    print(out.pop())
    
