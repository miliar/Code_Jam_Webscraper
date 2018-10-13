infile = "a-large.in"
outfile = "a-large.out"

lines = [l.strip() for l in open(infile,"r")]
from collections import defaultdict, Counter
from functools import partial

num_cases = int(lines[0])
lines = lines[1:]

cases = []

for _ in range(num_cases):
    
    N, X = map(int, lines[0].split())
    lines = lines[1:]
    sizes = map(int, lines[0].split())
    lines = lines[1:]
    
    case = N, X, sizes
    
    cases.append(case)
    
def process_case(case):
    
    n, x, sizes = case
    
    sizes.sort(reverse=True)
    #print n, x, sizes

    
    count = 0
    while True:
        if len(sizes) == 0:
            return count
        smallest = sizes.pop()
        #print smallest, sizes, count
        for i, size in enumerate(sizes):
            #print "checking", i, size
            if size + smallest <= x:
                matched = True
                sizes.pop(i)
                break
        
        count += 1

    return count
    
    
    return case

with open(outfile,"w") as g:
    
    for i, case in enumerate(cases):
        g.write("Case #" + str(i + 1) + ": " + str(process_case(case)) + "\n")
    

