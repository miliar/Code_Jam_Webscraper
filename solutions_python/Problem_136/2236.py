infile=open("large.in")
#from scipy import special
outfile=open("large.out", "a")
def output(num, count):
    outstr="Case #"
    outstr+=str(count+1)
    outstr+=": "
    outstr+=str(num)
    outstr+="\n"
    outfile.write(outstr)
    print count
N=int(infile.readline())

def calctime(C,F,X,farms):
    time=0
    rate=2
    for c1 in xrange(farms):
        time+=C/rate
        rate+=F
    time+=X/rate
    return time
def case():
    a=[float(y) for y in infile.readline().strip().split(" ")]
    c=1000000000
    m=0
    count=0
    while m<=c:
        m=calctime(a[0],a[1],a[2],count)
        if m<c:
            c=m
        count+=1
    return c
for x in xrange(100):
    output(case(), x)

    
