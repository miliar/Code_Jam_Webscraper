import re, sys
pat = re.compile(r'\s+')

def on_off(n,k):
    x= pow(2,n)
    if((k%x))==x-1: return True
    else: return False


def process(filename):
    f=open(filename)
    case, line_no = 0, 0
    
    for line in f:
        line_no+=1
        if(line_no==1):continue
        case+=1
        n,k = map(lambda(x):int(x),pat.split(line.strip()))
        res='OFF'
        if(on_off(n,k)): res='ON'
        print "Case #%d: %s"%(case,res)
    f.close()


process(sys.argv[1]) 


