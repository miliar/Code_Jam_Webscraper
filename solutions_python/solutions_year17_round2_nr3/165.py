def solve(lines):
    l1 = lines[0].split(" ")
    N = int(l1[0])
    Q = int(l1[1])
    i=1
    E = []
    S = []
    while i< N+1:
        l = lines[i].split(" ")
        E.append(int(l[0]))
        S.append(int(l[1]))
        i+=1
    graph = [[int(j) for j in line.split(" ")] for line in lines[i:i+N]]
    
    U = [int(line.split(" ")[0]) for line in lines[i+N:]]
    
    V = [int(line.split(" ")[1]) for line in lines[i+N:]]
    
    mintimes = [-1 for i in range(N)]
    mintimes[0] = 0
    i = 1
    while i<N:
        #print mintimes
        j = 0
        t = 0
        tmin = float("inf")
        while j<i:
            k=j
            dist = 0.0
            while k<i:
                dist += graph[k][k+1]
                k+=1
            
            if dist>E[j]:
                j+=1
                continue
            
            t = dist/S[j]
            tmin = min(t + mintimes[j],tmin)
            
            j+=1
        
        mintimes[i] = tmin
        
        i+=1
    
    return str(mintimes[N-1])
    #print E
    #print S
    #print graph
    #print U
    #print V
    
	
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
    N = int(lines[k].split(" ")[0])
    #print lines[k:k+N+1]
    ans = solve(lines[k:k+2*N+2])
    k+=2*N+2
    print "Case #"+str(i)+": "+ans