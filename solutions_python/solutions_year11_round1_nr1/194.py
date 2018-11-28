from fractions import Fraction

t = 0
fp = open("large.txt")  #input filename
fout = open("large_out.txt", "w") #output filename

lut = {}
def calc():
    for i in range(100, 0, -1):
        for j in range(100, 0, -1):
            lut[i/j*1.0+1] == 0;
    
def get_input():
    global t

    t = int(fp.readline())
    
    for i in xrange(t):
        line = fp.readline().split()
        n = int(line[0])
        pd = int(line[1])
        pg = int(line[2])
        yield n,pd,pg

def process(n, pd, pg):
    if (pg == 100 and pd <100) or (pg == 0 and pd >0):
        return "Broken"
    f=Fraction(pd, 100)
    if f.numerator > n or f.denominator > n:
        return "Broken"
    return "Possible"
    
for i,j in enumerate(get_input(), 1):
    n,pd,pg = j
    print n,pd,pg
    r = process(n,pd,pg)
    print "Case #%s: %s" % (i,r)
    print >> fout, "Case #%s: %s" % (i,r)
    
fout.close()
