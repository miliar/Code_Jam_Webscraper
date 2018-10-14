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


T = int(inp.readline())

for t in xrange(T):
    n = inp.readline().strip()
    clean = True
    if len(n) == 1:
        print_case(t+1, n)
        continue
    
    group_start = 0
    for i in xrange(1, len(n)):
        if n[i] < n[i-1]:
            clean = False
            rest = n[i:]
            nines = "9" * len(rest)
            digit = int(n[i-1]) - 1
            if digit == 0:
                print_case(t + 1, "9" * (len(n) - 1))
                break
            result = n[:group_start] + str(digit) + "9" * (len(n) - group_start - 1)
            print_case(t + 1, result)
            break
        if n[i] != n[i-1]:
            group_start = i
    
    if clean: 
        print_case(t+1, n)
       
        
    