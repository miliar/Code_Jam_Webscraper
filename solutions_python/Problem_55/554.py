import sys

filename = sys.argv[1]
f = open(filename)
output = open("result.txt","w")
times = int(f.readline())

for i in xrange(times):
    total = 0
    line = f.readline()
    R,k,N = [int(x) for x in line.split()]
    line = f.readline()
    groups = [int(x) for x in line.split()]
    l = len(groups);
    gsum = []
    for j in xrange(l):        
        s = groups[j]
        t = 1
        s1 = s+groups[(j+1)%l]
        while (s1 <= k) and t<l:
            s = s1
            t += 1
            s1 += groups[(j+t)%l]
        
        gsum.append([s,t])
        
    cur = 0
    total = 0
    for j in xrange(R):
        total += gsum[cur][0]
        cur = (cur+gsum[cur][1])%l

    output.write("Case #"+str(i+1)+": "+str(total)+"\n")
    
