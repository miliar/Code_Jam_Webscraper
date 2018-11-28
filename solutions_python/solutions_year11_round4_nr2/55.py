# -*- coding: utf-8 -*-
fname = "B-small-attempt1"
fin = open(fname+".in","r")
fout = open(fname+".out","w")
def gcj_read():
  linestr = fin.readline().strip()
  return [int(numb) for numb in linestr.split()]

numcases = gcj_read()[0]

for caseno in range(numcases):
    R, C, D = gcj_read()
    grid = []
    for r in range(R):
        rstr = fin.readline().strip()
        grid.append([D+int(x) for x in rstr])
    
    maxodd_r = 0
    maxeven_r = 1
    for r in xrange(1, R-1):
        for c in xrange(1, C-1):
            #print (R, C), (r, c)
            maxpossodd_r = min(r, c, R-1-r, C-1-c)
            maxposseven_r = min(r, c, R-r, C-c)
            #print maxpossize, maxsize, caseno
            
            # Odd widths
            for a in xrange(maxodd_r+1, maxpossodd_r+1):
                weighted_x, weighted_y = 0, 0
                corners = set([(r-a, c-a), (r-a, c+a), (r+a, c-a), (r+a, c+a)])
                for x in xrange(r-a, r+a+1):
                    for y in xrange(c-a, c+a+1):
                        if (x, y) in corners:
                            #print (x,y), "Corner"
                            continue
                        #print (x,y),
                        #print a, (r,c), (x, y), maxpossize
                        m = grid[x][y]
                        weighted_x += (x - r) * m
                        weighted_y += (y - c) * m
                if (r, c) == (3, 4):
                    print
                    print weighted_x, weighted_y, a
                if weighted_x == 0 and weighted_y == 0:
                    maxodd_r = maxeven_r = a
            
            # Even widths
            for a in xrange(maxeven_r+1, maxposseven_r+1):
                weighted_x, weighted_y = 0, 0
                corners = set([(r-a, c-a), (r-a, c+a-1), (r+a-1, c-a), (r+a-1, c+a-1)])
                for x in xrange(r-a, r+a):
                    for y in xrange(c-a, c+a):
                        if (x, y) in corners:
                            continue
                        m = grid[x][y]
                        weighted_x += (0.5 + x - r) * m
                        weighted_y += (0.5 + y - c) * m
                if weighted_x == 0 and weighted_y == 0:
                    maxeven_r = a
                    maxodd_r = a - 1
    
    if maxodd_r == 0:
        outstr = "IMPOSSIBLE"
    elif maxeven_r > maxodd_r:
        # Largest size was even
        outstr = str(maxeven_r * 2)
    else:
        # Largest size was odd
        outstr = str(1 + (maxodd_r * 2))
    fout.write("Case #"+str(caseno+1)+": "+ outstr +"\n")

fin.close()
fout.close()
