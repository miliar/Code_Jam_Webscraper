from sys import stdin

def solve(num):
    numstr = [int(x) for x in str(num)]
    i = 1
    while i < len(numstr):
        if numstr[-i] < numstr[-i-1]:
            num = int("".join(str(x) for x in numstr[:-i])) - 1
            numstr = [int(x) for x in str(num)] + [9 for _ in numstr[-i:]]
        i += 1
    return int("".join(str(x) for x in numstr))
def parse(input):
    t = int(input.next())
    
    for i in range(t):
        n = int(input.next())
        res = solve(n)
        
        print "Case #%d: %s" % (i+1, "IMPOSSIBLE" if res is None else res)
	
parse(stdin)