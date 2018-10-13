import sys, math

sys.setrecursionlimit(2500)

from collections import Counter

inp = open("in.txt")
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


t = int(inp.readline())

def flip_first_k(pancakes, k):
    result = ""
    if len(pancakes) < k:
        return "-"
    for i in xrange(k):
        if pancakes[i] == "-":
            result += "+"
        else:
            result += "-"
    
    result += pancakes[k:]
    return result

def flip_pancakes(pancakes, k, n=0):
    if len(pancakes) <= k and 0 < pancakes.count("-") < k:
        return -1
    for i in xrange(len(pancakes)):
        if pancakes[i] == "-":
            pancakes = flip_first_k(pancakes[i:], k)
            return flip_pancakes(pancakes, k, n+1)
    
    return n

for i in xrange(t):
    try:
        pancakes, k = inp.readline().split()
        k = int(k)
        n = flip_pancakes(pancakes, k)
        print_case(i+1, str(n) if n > -1 else "IMPOSSIBLE")
    except:
        raise 
        
    