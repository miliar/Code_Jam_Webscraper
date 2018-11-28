#universal dictionary
cdict={}
def builddict():
    f1 = open('test.txt','r')
    f2 = open('translate.txt','r')
    n = int(f1.readline())
    for i in range(0,n):
        ln1=f1.readline()
        ln2=f2.readline()
#        print ln1
#        print ln2
        keys=list(ln2)
        letters=list(ln1)
        count=0
        for x in letters:
            cdict[x]=keys[count]
#            print "assigninng",x,"to ",letters[count]
            count=count+1
#    print cdict

def runsol():
    fname='small.txt'
    f = open(fname,'r')
    fout = open('out.txt','w')
    n = int(f.readline())
    case=0
    for i in range(0,n):
        case=case+1
        fout.write('Case #'+str(case)+': ')
        ln=f.readline()
        letters=list(ln)
        for x in letters:
            fout.write(cdict[x])
    
        
if __name__ == "__main__":
    builddict()
    runsol()
