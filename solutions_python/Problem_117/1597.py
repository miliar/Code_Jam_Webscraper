import re
import math
import itertools

def config (lawn):
    t = len(lawn)
    c = len(lawn[0])
    rowmax = [ max(x) for x in lawn]
    cols = [[lawn[i][j] for i in range(t)] for j in range (c)]
    colmax = [max(x) for x in cols]
    for i in range(t):
	for j in range(len(lawn[i])):
	    value = lawn[i][j]
	    if value != rowmax[i] and value != colmax[j]:
		return "NO"
    return "YES"

def main ():
    output = []
    with open ("B-large.in", "r") as f:
	trials = f.readline()
	for i in range(int(trials.strip())):
	    dims = re.split (" ", f.readline())
    	    x = int(dims[1])
            y = int(dims[0])
            lawnmover = []
            for j in range(y):
	        line = f.readline()
	        nums = [ int(x.strip()) for x in re.split(" ", line)]
	        lawnmover.append(nums)
   	    condition = lawnmover
	    outline = "Case #%d: %s" % (i+1, config(condition))
	    print outline
	    output.append(outline)
    with open ("fucklawnlawnlawnlawn.out", "w") as f:
	f.write ("\n".join(output))

if __name__ == "__main__":
    main()
