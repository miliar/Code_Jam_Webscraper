File=open("B-large.in","r")
data=File.read().splitlines()
result=""
ans=0
dete=False
for i in data[1:]:
    temp=i.split(" ")
    C=float(temp[0])
    F=float(temp[1])
    X=float(temp[2])
    #print C,F,X
    n=0
    dete=0
    t=0
    temp2=[]
    rate=2+(n*F)
    if float(X)<float(C) :
        ans=float(X)/2
    else:
        temp2.append(t+(float(X)/rate))
        t=t+(float(C)/rate)
        n+=1
        rate=2+(n*F)
        temp2.append(t+(float(X)/rate))
        while float(temp2[-1]) < float(temp2[-2]):
            t=t+(float(C)/rate)
            n+=1
            rate=2+(n*F)
            temp2.append(t+(float(X)/rate))
            #print temp2
        ans=float(temp2[-2])
            
    result=result+"Case #"+str(int(len(result.splitlines()))+1)+": "+str(ans)+" \n"
    print result
print result
        
