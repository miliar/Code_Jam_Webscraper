
f=open("B-large.in.txt")
o=open("output.txt","w")
t=int(f.readline())
line=f.readline()
case=1
while line:
    outLine="Case #%d: "%case
    line=line.split()
    N=int(line[0])      #number of people
    S=int(line[1])      #number of surprising cases
    p=int(line[2])      #best score requirement
    T=[]
    for i in range(3,len(line)):
        T.append(int(line[i]))
    s=0
    result=0
    for i in range(len(T)):    
        if T[i]>3*p-5 and T[i]>0:
            if T[i]>=3*p-2:
                result+=1               
            else:
                if s+1<=S:
                    s+=1
                    result+=1
        elif p==0:
            result+=1
    outLine+=str(result)
    o.write(outLine)
    o.write('\n')
    case+=1
    line=f.readline()
f.close()
o.close()
