import sys, math

sys.setrecursionlimit(2500)

from collections import Counter

inp = open("in.txt")
#out = sys.stdout
out = open("out.txt","w+")

def print_case(case, result):
    debug("Case #%d: %s" % (case, str(result)))
    out.write("Case #%d: %s\n" % (case, str(result)))

def debug(message):
	if len(sys.argv) > 1 and sys.argv[1] == "silent":
		return
	sys.stdout = sys.__stdout__
	print message
	sys.stdout = out

T = int(inp.readline())

for t in xrange(T):
    r, c = [int(x) for x in inp.readline().split()]
    grid = []
    for i in xrange(r):
        grid.append(inp.readline().strip())
        
    outg = []
    empty = 0
    for row in grid:
        q = row.count("?")
        if q == 0:
            outg.append(row)
        elif q == c:
            if len(outg) == 0:
                empty += 1
            else:
                outg.append(outg[-1])
        else:
            res = ""
            rempty = 0
            for i in xrange(c):
                if row[i] == "?":
                    rempty += 1
                else:
                    res += (rempty + 1) * row[i]
                    rempty = 0
            res += rempty * res[-1]
            outg.append(res)
    
    outg = empty * [outg[0]] + outg
    
    print_case(t+1, "\n" + "\n".join(outg))
    
    
