import sys

import psyco; psyco.full()

def main():
    f = open(sys.argv[1], "rb")
    ncases = int(f.readline())
    for caseno in xrange(ncases):
        r, c = [int(x) for x in f.readline().strip().split()]
        
        lines = []
        locs = {}
        for y in xrange(r):
            line = f.readline().strip()
            lines.append(list(line))
            for x in xrange(c):
                if lines[y][x] != "?":
                    locs[lines[y][x]] = (y, x)
                        
        # fill to the right
        for ch in locs:
            y, x = locs[ch]
            x += 1
            while x < c and lines[y][x] == "?":
                lines[y][x] = ch
                x += 1
            
        # fill to the left
        for y in xrange(r):
            fill = "?"
            for x in xrange(c-1, -1, -1):
                if lines[y][x] != "?":
                    fill = lines[y][x]
                else:
                    lines[y][x] = fill
                
        # fill down
        fill = "?" * c
        for y in xrange(r):
            if "".join(lines[y]) != "?" * c:
                fill = lines[y]
            else:
                lines[y] = fill
                
        # fill up
        fill = "?" * c
        for y in xrange(r-1, -1, -1):
            if "".join(lines[y]) != "?" * c:
                fill = lines[y]
            else:
                lines[y] = fill
        
        print "Case #%d:" % (caseno + 1)
        for i in xrange(r):
            print "".join(lines[i])
        
main()