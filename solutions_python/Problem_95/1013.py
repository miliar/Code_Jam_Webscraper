dataOfGg={'a':'y','b':'h','c':'e','d':'s','e':'o','f':'c','g':'v',
      'h':'x','i':'d','j':'u','k':'i','l':'g','m':'l','n':'b',
      'o':'k','p':'r','q':'z','r':'t','s':'n','t':'w','u':'j',
      'v':'p','x':'m','w':'f','y':'a','z':'q',' ':' '}


def readInput():
    f=open('A-small-attempt0.in','r')
    n=int(f.readline())
    i=1
    while (i<=n):
        s=f.readline()
        process(s,i)
        i+=1
    f.close()    
     
def process(s,caseNumber):
    out=''
    for t in s:
        if (t!='\n'):
            out=out+dataOfGg[t]
    writeOutput(out,caseNumber)

def writeOutput(s,caseNumber):
    if int(caseNumber)==1:
        f=open("Output.txt","w")
        f.write('Case #1: {0:s}\n'.format(s))
        f.close()
    else:
        f=open("Output.txt","a")
        f.write('Case #{0:d}: {1:s}\n'.format(int(caseNumber),s))
        f.close()
    
if __name__=='__main__':
    readInput()
