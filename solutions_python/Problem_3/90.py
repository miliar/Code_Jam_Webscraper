# outer radius Ro, thickness t, Ri = Ro-t
# cylinder of radius r each string
# gap g between strings

# fly is a sphere of radius f

import math
import jamio

from decimal import *

def get_input():
    ret = []
    lines = jamio.get_file_lines()
    n = int(lines[0])
    for i in range(n):
        ret += [map(float, lines[i+1].split(' '))]
    return ret

def probability(casex):
    [rfly,router,thickness,rstring,gap] = casex
    #print rfly,router,thickness,rstring,gap

    gap = gap - 2*rfly
    rstring = rstring + rfly
    dstring = 2*rstring
    rinner = router - thickness - rfly
    
    #print gap
    if gap<=0:
        return 1.000000
    
    if rfly<=0:
        return 1.000000

    debugs = """\
the fly radius:\t\t%s
the inner radius:\t%s
the outer radius:\t%s
the string radius:\t%s
the gap:\t\t%s
    """% (rfly,rinner,router,rstring,gap)
    
    #print debugs

    space = 0.0
    fullgrid = gap**2

    # n loops
    n = int(math.ceil(rinner/(gap+dstring)) + 1)
    
    m = int(rinner/(math.sqrt(2)*(gap+dstring)))

    #   a   b  
    #
    #   c   d
    
    # full grids
    space += fullgrid*m*m
    
    #print space

    def square(x, more=0):
        return distance(x, more)**2

    def distance(x, more=0):
        return ((x-1)*(gap+dstring)+rstring+more)
    
    def smalls(x):
        afa = math.asin(x/rinner/2.0)            
        return float(afa*(rinner**2) - math.sqrt(rinner**2-(x/2.0)**2)*x/2.0)        

    ri2 = rinner**2
    
    for i in range(1,n+11):
        for j in range(1,n+11):
            #print i,j
            if i<=m and j<=m:
                continue
            #print j*(700)
            # invisible 
            if square(i)+square(j)>=ri2:
                #print "c0"
                continue  
            # totally visible
            if square(i,gap)+square(j,gap)<=ri2:
                space += fullgrid
                continue
            # a,c are visible
            if square(i)+square(j,gap)<=ri2 and square(i,gap)+square(j)>=ri2:
                #b1 = distance(i,gap) - math.sqrt(ri2 - square(j,gap))
                #b2 = distance(i,gap) - math.sqrt(ri2 - square(j))
                #space += fullgrid - float((b1+b2)*gap)/2.0 + smalls(math.sqrt((b1-b2)**2+gap**2))
                b1 = math.sqrt(ri2-square(j,gap)) - distance(i)
                b2 = math.sqrt(ri2-square(j))- distance(i)
                space += float((b1+b2)*gap)/2.0 + smalls(math.sqrt((b1-b2)**2+gap**2))
                continue
            # c,d are visible
            if square(i)+square(j,gap)>=ri2 and square(i,gap)+square(j)<=ri2: 
                #b1 = distance(j,gap) - math.sqrt(ri2 - square(i,gap))
                #b2 = distance(j,gap) - math.sqrt(ri2 - square(i))
                #space += fullgrid - float((b1+b2)*gap)/2.0 + smalls(math.sqrt((b1-b2)**2+gap**2))
                b1 = math.sqrt(ri2-square(i,gap)) - distance(j)
                b2 = math.sqrt(ri2-square(i))- distance(j)
                space += float((b1+b2)*gap)/2.0 + smalls(math.sqrt((b1-b2)**2+gap**2))
                continue
            # c,a,d are visible
            if square(i)+square(j,gap)<=ri2 and square(i,gap)+square(j)<=ri2: 
                b1 = distance(i,gap) - math.sqrt(ri2 - square(j,gap))
                b2 = distance(j,gap) - math.sqrt(ri2 - square(i,gap))
                #print b1,b2
                space += fullgrid - float(b1*b2)/2.0 + smalls(math.sqrt(b1**2+b2**2))
                continue 
            # only c is visible  :0k
            if square(i)+square(j,gap)>=ri2 and square(i,gap)+square(j)>=ri2:
                #print "c5"
                #print i,j
                b1 = math.sqrt(ri2 - square(i)) - distance(j)
                b2 = math.sqrt(ri2 - square(j)) - distance(i)
                space += float(b1*b2)/2.0+smalls(math.sqrt(b1**2+b2**2))
                continue
    
    return 1-(space*4)/(math.pi*(router**2))


    
text = ""
cases = get_input()
for i in range(len(cases)):
    text += "Case #%d: %f\n" % (i+1,probability(cases[i]))
    

jamio.output(text)
