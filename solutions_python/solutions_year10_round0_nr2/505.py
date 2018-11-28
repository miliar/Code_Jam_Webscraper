import fractions
def calculate(l):
    l.sort()
    min = l[0]
    #print l
    for i in range(0,len(l)):
        l[i] = l[i]-min
    #print l
    divv = l[1]
    for i in range(1,len(l)):
        if l[i]!=0:
            divv = fractions.gcd(divv,l[i])
    if len(l)==2:
        divv = l[1]
    if divv==0 or divv==1 or divv==min: 
        return 0
    #print divv
    for i in range(1,len(l)):
        if(l[i]%divv!=0):
            return 0
    if min%divv==0:
        return 0
    return (((min/divv)+1)*divv)-min

f = open('B-large.in','r')
count = 0
for l in f:
    if count!=0:
        d = [int(k) for k in l.split(" ")]
        print "Case #%d: %d" % (count,calculate(d[1:]),)
    count = count+1
f.close()
