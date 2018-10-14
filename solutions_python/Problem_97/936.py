def readInput():
    f=open('C-small-attempt0.in','r')
    n=int(f.readline())
    for i in range(1,n+1):
        s=f.readline()
        pos=s.find(' ')
        A=int(s[0:pos])
        B=int(s[pos:])
        process(A,B,i)
    f.close()

def process(A,B,caseNumber):
    ds=[]
    for i in range(A,B+1):
        s=str(i)
        for j in range(1,len(s)):
            n=s[len(s)-j:]+s[0:len(s)-j]
            if (n,s) in ds or (s,n) in ds:
                continue
            elif int(n)<B and int(n)>A and int(n)!=i:
                ds.append((n,s))
    count=len(ds)
#    print(ds)
    writeOutput(count,caseNumber)
                
    
def writeOutput(n,caseNumber):
    if int(caseNumber)==1:
        f=open('output.out','w')
        f.write('Case #1: {0:d}\n'.format(n))
        f.close()
    else:
        f=open('output.out','a')
        f.write('Case #{0:d}: {1:d}\n'.format(caseNumber,n))
        f.close()
        
if __name__=='__main__':
    readInput()