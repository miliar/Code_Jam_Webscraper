def readInput():
    f=open('B-large.in','r')
    n=int(f.readline())
    for i in range(1,n+1):
        s=f.readline()
        process(s,i)
    f.close()
    
def stringProcess(s):
    l=[]
    t=0
    p=0
    while (t!=-1):
        t=s.find(' ',p,len(s))
        if t==-1:
            l.append(int(s[p:]))
        else:
            l.append(int(s[p:t]))
            p=t+1
    return l

def process(s,caseNumber):
    ds=stringProcess(s)
    n=0
    for i in range(3,len(ds)):
        if ds[i]>=ds[2]:
            if (ds[i]/3)>=ds[2] or ((ds[i]+2)/3)>=ds[2]:
                n+=1
            elif ds[1]>0 and ((ds[i]+4)/3)>=ds[2]:
                n+=1
                ds[1]-=1
            else:
                continue
    writeOutput(n,caseNumber)
            
    

def writeOutput(n,caseNumber):
    if int(caseNumber)==1:
        f=open('output.b','w')
        f.write('Case #1: {0:d}\n'.format(n))
        f.close()
    else:
        f=open('output.b','a')
        f.write('Case #{0:d}: {1:d}\n'.format(caseNumber,n))
        f.close()
    
if __name__=='__main__':
    readInput()