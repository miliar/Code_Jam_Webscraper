import sys
import time

t0 = time.time()
args = sys.argv[1:]
input = args[0]
output = args[1]

cases = [ line.strip().split() for line in open(input).readlines()[1:] ]

solution = []
for case in cases:
    aud = map(int, case[1])
    req = 0
    for i in range(len(aud)):
        smax = i
        total = sum(aud[:i])
        needed = smax - (total+req)
        if needed > 0:
            req = req+needed
    solution.append(req)

outfile = open(output, "w")
for i in range(len(solution)):
    outfile.write("Case #"+str(i+1)+": "+str(solution[i])+"\n")
t1 = time.time()
print str(t1-t0)
