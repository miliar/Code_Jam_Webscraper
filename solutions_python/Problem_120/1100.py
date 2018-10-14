from math import pi
fin = open("rings.in")
fout = open("rings.out","w")
cases = int(fin.readline())

def pp(case, out):
    ss= "Case #%d: %s\n" % (case+1, out)
    print ss,
    fout.write(ss)

def calc(paint, r):
    top = .5*((8*paint+1)**.5-1)
    return top
    
def cal2(r):
    return r**2-(r-1)**2
for case in xrange(cases):
    rad, paint = map(int, fin.readline().split(" "))
    #paint/=pi
    #times = calc(paint, r)
    rad+=1
    times = 0
    #print "i start with radius", rad
    #print "paint required for first circle", cal2(rad)
    while paint>=cal2(rad):
        paint-=cal2(rad)
        rad+=2
        times+=1
    pp(case,times)


    
    
"""
cost of circles increases by r**2-(r-1)**2 each time
"""
