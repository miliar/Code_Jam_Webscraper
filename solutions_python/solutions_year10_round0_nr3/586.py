filename = "C-small-attempt0.in"
f = open (filename)
outfile = open (filename.rsplit(".", 1)[0] + ".out", 'w')

T = int(f.readline())

for i in xrange (T):
    profit = 0
    inlist = [int(x) for x in f.readline().split(" ")]
    R = inlist[0]
    k = inlist[1]
    N = inlist[2]
    g = [int(x) for x in f.readline().split(" ")]
   

    for j in xrange (R):
        coaster = []
        g.reverse()
        while (len(g) > 0) and (sum(coaster) + g[-1] <= k):
            coaster.append(g.pop())

        profit += sum(coaster)
        
        g.reverse()
        g += coaster            
    



    outfile.write("Case #%d: %d\n" % (i+1, profit))



f.close()
outfile.close()
