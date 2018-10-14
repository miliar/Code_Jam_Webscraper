global a
a=open("A-small-attempt0.in","r")
def NumOfDisks(r,t):
    i=0
    count=0
    while(1==1):
        s=2*r+4*i+1
        if(s<=t):
            t-=s
            count+=1
        else:
            break
        i+=1
    return count
line=a.readline()
T=int(line[:len(line)-1])
i=1
results=[]
while(i<=T):
    line=a.readline()
    if(line[len(line)-1]=='\n'):
        line=line[:len(line)-1]
    firstnum=""
    lastnum=""
    isAfterSpace=False
    j=0
    while(j<len(line)):
        if(line[j]!=" "):
            if(isAfterSpace==False):
                firstnum+=line[j]
            else:
                lastnum+=line[j]
        else:
            isAfterSpace=True
        j+=1
    r=int(firstnum)
    t=int(lastnum)
    results+=[NumOfDisks(r,t)]
    i+=1
i=1
while(i<=T):
    print("Case #"+str(i)+": "+str(results[i-1]))
    i+=1
