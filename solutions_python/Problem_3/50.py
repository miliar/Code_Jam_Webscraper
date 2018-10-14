import math
from math import atan
from math import sqrt
#from math import pow

def surfprimitive(x, r):
    s = sqrt(pow(r, 2.0) - pow(x, 2.0))
    if s==0:
        return 0.5 * ( (math.pi/2.0) * pow(r, 2.0) + (x*s) )
    else:
        return 0.5 * ( atan(x/s) * pow(r, 2.0) + (x*s) )

def integrate(x1,x2,r):
    return surfprimitive(x2,r)-surfprimitive(x1,r)

def surface(x1,y1,W,R):
    x2=x1+W
    y2=y1+W
    if isincircle(x2,y2,R)>=0:
        #simple case
        return pow(W, 2.0)
    else:
        topleftin = (isincircle(x1,y2,R)>0)
        bottomrightin = (isincircle(x2,y1,R)>0)
        if not topleftin and not bottomrightin:
            xmiddle=sqrt(pow(R, 2.0) - pow(y1, 2.0))
            return integrate(x1,xmiddle,R) - y1*(xmiddle-x1)
        if topleftin and bottomrightin:
            xmiddle=sqrt(pow(R, 2.0) - pow(y2, 2.0))
            return W*(xmiddle-x1)+integrate(xmiddle,x2,R)-(x2-xmiddle)*y1
        if topleftin and not bottomrightin:
            xmiddle1=sqrt(pow(R, 2.0) - pow(y2, 2.0))
            xmiddle2=sqrt(pow(R, 2.0) - pow(y1, 2.0))
            return W*(xmiddle1-x1)+integrate(xmiddle1,xmiddle2,R)-(xmiddle2-xmiddle1)*y1
        if not topleftin and bottomrightin:
            return integrate(x1,x2,R)-W*y1



def isincircle(x,y,r):
    return pow(r, 2.0) - (pow(x, 2.0) + pow(y, 2.0))

fin = open(r'C:\Ggl\qual\C-small-attempt0.in')

numcases=int(fin.readline())
for case in range(numcases):
    line=fin.readline().strip()

    (f, R, t, r, g) = map(float, line.split(' '))
    
    totalsurface = math.pi * pow(R,2.0) / 4.0
    emptysurface = 0.0
    
    squareW = g - (2*f)
    stringW = 2*r + 2*f
    surfaceR = R - t - f
    
    if squareW!=0:
        i = 0
        j = 0
        while True:
            x1 = stringW/2 + (squareW+stringW)*i
            x2 = x1 + squareW
            y1 = stringW/2 + (squareW+stringW)*j
            y2 = y1 + squareW

            if isincircle(x1,y1,surfaceR)<=0:
                if i==0: break
                i = 0
                j += 1
                continue

            emptysurface += surface(x1,y1,squareW,surfaceR)

            i += 1

    print "Case #" + str(case+1) + ": " + ('%0.6f' % (1-emptysurface/totalsurface))
            

        






