import sys, random

import psyco; psyco.full()

def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline().strip())
    
    for caseno in xrange(ncases):
        a, b, c = f.readline().strip().split()
        
        numcirc = int(a)
        width = int(b)
        length = int(c)
        
        circles = []
        
        index = 0
        for r in f.readline().strip().split():
            circles.append((int(r), index))
            index += 1
            
        circles.sort()
        
        circles = circles[::-1]
        placed = []
        placed.append((0,0,circles[0][0]))
        xdir = 1
        ydir = 0
        
        if len(circles) > 1:
            for i in xrange(1, len(circles)):
                prevrad = circles[i-1][0]
                currrad = circles[i][0]
                
                dist = prevrad+currrad
                
                foundpos = False
                for j in xrange(4):
                    newx = placed[i-1][0] + dist * xdir
                    newy = placed[i-1][1] + dist * ydir
                    
                    ok = True
                    if newx >= 0 and newx <= width and newy >= 0 and newy <= length:
                        for compx, compy, prevrad in placed:
                            dx = abs(newx-compx)
                            dy = abs(newy-compy)
                            dz = prevrad+currrad
                            
                            if dx * dx + dy * dy < dz * dz:
                                ok = False
                                break
                                
                    else:
                        ok = False
                        
                    if ok:
                        placed.append((newx,newy,currrad))
                        foundpos = True
                        break
                    else:
                        xdir, ydir = ydir * -1, xdir * 1
                        
            if not foundpos:
                raise Exception("DSDSDDS")
            
        results = [None] * len(circles)
        for i in xrange(len(circles)):
            x,y,r = placed[i]
            results[circles[i][1]] = (x,y,r)
            
        #print results
        s = ""
        for x,y,r in results:
            s += " %.1f %.1f" % (x, y)
            
        print "Case #%d:%s" % (caseno+1, s)
                    
main()