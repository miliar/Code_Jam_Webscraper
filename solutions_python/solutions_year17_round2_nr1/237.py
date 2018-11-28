def solve(ls):
    lines =ls
    D = int(lines[0].split(" ")[0])
    K = [int(line.split(" ")[0]) for line in lines[1:]]
    S = [int(line.split(" ")[1]) for line in lines[1:]]
    t = 0.0
    tmax = -1
    for i in range(len(K)):
        t = float(D-K[i])/S[i]
        if tmax<t:
            tmax = t
    
    maxspeed = D/tmax
    return str(maxspeed)
	
import sys
filename = sys.argv[1]
f = open(filename, "r")
s = f.read()
f.close()
lines = s.split("\n")
lines = [l.strip() for l in lines]
T = int(lines[0])
k=1
for i in range(T+1):
    if i==0:
        continue
    N = int(lines[k].split(" ")[1])
    #print lines[k:k+N+1]
    ans = solve(lines[k:k+N+1])
    k+=N+1
    print "Case #"+str(i)+": "+ans