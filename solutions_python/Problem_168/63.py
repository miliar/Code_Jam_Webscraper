import sys

import psyco; psyco.full()

def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline())
    for caseno in xrange(ncases):
        r, c = f.readline().split()
        r = int(r)
        c = int(c)
        
        grid = []
        for i in xrange(r):
            grid.append(f.readline().strip())
            
        count = 0
        good = True
        for y in xrange(r):
            for x in xrange(c):
                ch = grid[y][x]
                if ch == ".":
                    continue
                    
                cands = ""
                for xd,yd,ca in ((0,-1,"^"),(0,1,"v"),(-1,0,"<"),(1,0,">")):
                    xx = x
                    yy = y
                    while True:
                        xx += xd
                        yy += yd
                        if xx < 0 or xx >= c or yy < 0 or yy >= r:
                            break
                        if grid[yy][xx] != ".":
                            cands += ca
                            break
                
                if len(cands) == 0:
                    good = False
                else:
                    if ch not in cands:
                        count += 1
                        
        
        if good:
            s = int(count)
        else:
            s = "IMPOSSIBLE"
            
        print "Case #%d: %s" % (caseno+1, s)
                    
        
main()