import math
def findNums(N):
    if N%2==1:
        return str((N-1)/2) + " " + str((N-1)/2)
    else:
        return str(N/2) + " " + str(N/2 - 1)

def solve(line):
    l = line.split(" ")
    n = int(l[0])
    k = int(l[1])
    
    a = int(math.floor(math.log(k,2)))
    r = int(k - 2**a + 1)
    
    
    i=0
    splitSizes = [0,0]
    splitCount = [1,1]
    
    if n%2==0:
        splitSizes[0] = n/2 - 1
        splitSizes[1] = n/2
    else:
        splitSizes[0] = (n-1)/2
        splitSizes[1] = (n+1)/2
        splitCount[0] = 2
        splitCount[1] = 0
    
    while i<a-1:
        s1 = splitSizes[0]
        s2 = splitSizes[1]
        c1 = splitCount[0]
        c2 = splitCount[1]
        if s1%2==1:
            splitSizes[0] = (s1-1)/2
            splitSizes[1] = splitSizes[0] + 1
            splitCount[0] = 2*c1 + c2
            splitCount[1] = c2
        else:
            splitSizes[0] = s1/2 - 1
            splitSizes[1] = s1/2
            splitCount[0] = c1
            splitCount[1] = 2*c2 + c1
        i+=1
     
    #print splitSizes, splitCount, r
           
    if k==1:
        return findNums(n)
    
    if r>splitCount[1]:
        return findNums(splitSizes[0])
    else:
        return findNums(splitSizes[1])
    
		
import sys
filename = sys.argv[1]
f = open(filename, "r")
s = f.read()
f.close()
lines = s.split("\n")
lines = [l.strip() for l in lines]
T = int(lines[0])
for i in range(T+1):
    if i==0:
        continue
    line = lines[i]
    ans = solve(line)
    print "Case #"+str(i)+": "+ans