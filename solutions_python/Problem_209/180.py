import math
def solve(lines):
    N = int(lines[0].split(" ")[0])
    K = int(lines[0].split(" ")[1])
    
    RH = [(int(lines[k].split(" ")[0]),2*math.pi*int(lines[k].split(" ")[0])*int(lines[k].split(" ")[1]),k) for k in range(1,N+1,1)]

    RH = sorted(RH, key = lambda x:x[0])
    HR = sorted(RH,key = lambda x:x[1])
    RH = RH[::-1]
    #print RH
    #print RH
    area = 0
    maxarea = 0
    for i in range(N):
        
        r = RH[i][0]
        area = math.pi*r*r + RH[i][1]
        
        #key = RH[i][2]
        remaining = RH[i+1:]
        rem = sorted(remaining,key = lambda x:x[1])[::-1]
        #print rem
        
        #for k in range(N):
        #    if HR[k][2] == key:
        #        index = k
        #        break
                
        for j in range(K-1):
            if j>=len(remaining):
                break
            area+=rem[j][1]
        
        maxarea = max(maxarea,area)
    
    return str(maxarea)
       
import sys
filename = sys.argv[1]
f = open(filename, "r")
s = f.read()
f.close()


lines = s.split("\n")
lines = [l.strip() for l in lines]
T = int(lines[0])
j=1
for i in range(1,T+1,1):
	l = lines[j]
	R = int(l.split(" ")[0])
	IN = lines[j:j+1+R]
	j+=R+1
	ans = solve(IN)
	print "Case #"+str(i)+": "+ans