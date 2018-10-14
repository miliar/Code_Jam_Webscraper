testcase = """5
0.25 1.0 0.1 0.01 0.5
0.25 1.0 0.1 0.01 0.9
0.00001 10000 0.00001 0.00001 1000
0.4 10000 0.00001 0.00001 700
1 100 1 1 10"""

import math

def area_chord(R,r):
    if r >= R:
            return 0
    return R*R*math.acos(r/R)-r*math.sqrt(R*R-r*r)
def area_stripe(R,a,b):
    return area_chord(R,min(a,b))-area_chord(R,max(a,b))
def area_chorded_rect(R,ax,ay,bx,by):
    #   d1 d2
    #   d0 d3
    # O
    d0 = math.sqrt(ax*ax+ay*ay)
    d1 = math.sqrt(ax*ax+by*by)
    d2 = math.sqrt(bx*bx+by*by)
    d3 = math.sqrt(bx*bx+ay*ay)
    if d0 >= R:
        a = 0
    elif d2 <= R:
        a = (bx-ax)*(by-ay)
    elif d1 > R and d3 < R:
        sa = area_stripe(R,ax,bx)
        ra = (bx-ax)*ay
        a = sa/2.0-ra
    elif d1 < R and d3 < R:
        axp = math.sqrt(R*R-by*by)
        sa = area_stripe(R,axp,bx)
        ra = (bx-axp)*ay
        rap = (axp-ax)*(by-ay)
        a = (sa/2.0-ra)+rap
    elif d1 > R and d3 > R:
        bxp = math.sqrt(R*R-ay*ay)
        sa = area_stripe(R,ax,bxp)
        ra = (bxp-ax)*ay
        a = sa/2.0-ra
    else: # d1 < R and d3 > R
        sa = area_stripe(R,ay,by)
        ra = (by-ay)*ax
        a = sa/2.0-ra
    if a < 0:
            print "negative area", a, "---", R, d0, d1, d2, d3
    return a
def probability_dead_fly(f,R,t,r,g):
    if 2*f >= g:
        return 1.0
    d = g-2*f # actual rectangle size we're looking for
    Radj = R-t-f # actual circle radius for slot area calculation
    
    ta = 0
    x = r
    while (x < R):
        y = r
        while (y < R):
            a = area_chorded_rect(Radj,x+f,y+f,x+g-f,y+g-f)
            if a < 0:
                print "neg area", Radj, x+f, y+f
            #print "...", a
            ta += a
            y += g+2*r
        x += g+2*r
    ta *= 4
    ca = math.pi*R*R
    return (ca-ta)/ca

#lines = testcase.splitlines()
lines = open("C-large.in").readlines()
ntestcases = int(lines[0])
i = 0
for line in lines[1:]:
    f,R,t,r,g = tuple([float(x) for x in line.split()])
    print "Case #%d: %f" % (i+1, probability_dead_fly(f,R,t,r,g))
    i += 1

