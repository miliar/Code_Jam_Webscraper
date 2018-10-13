from sys import stdin

def solve(s_original, k):
    
    #cache of previously solved positions
    cache = {}
    
    def solve_inner(s):
        #if we hit this in the cache, we've returned to the original point, so obviously not optimal
        cache[s] = None
        
        if "-" not in s:
            return 0

        best = None
        for i in range(len(s)+1-k):
            new_s = s[:i] + "".join(["+" if x=="-" else "-" for x in s[i:i+k]]) + s[i+k:]
            #print new_s
            
            if new_s in cache:
                res = cache[new_s]
            else:
                res = solve_inner(new_s)
                cache[new_s] = res
            if res is not None and (best is None or res + 1 < best):
                best = res + 1
        return best
    
    return solve_inner(s_original)
	
def parse(input):
    t = int(input.next())
    
    for i in range(t):
        line = input.next().split(" ")
        s = line[0]
        k = int(line[1])

        res = solve(s,k)
        
        print "Case #%d: %s" % (i+1, "IMPOSSIBLE" if res is None else res)
		
parse(stdin)