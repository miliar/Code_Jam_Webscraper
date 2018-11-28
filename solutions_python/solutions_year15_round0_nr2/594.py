import math
infile = open('B-large.in','r')
outfile = open('output.txt', 'w')

T = int(infile.readline().strip())
out = ""
for tc in range(T):
    out += "Case #"+str(tc+1)+": "
    
    #solution here
    D = int(infile.readline().strip())
    P = map(int,infile.readline().strip().split())
    pancakes = [0 for x in range(1001)] # 0 index unused
    for p in P:
        pancakes[p] += 1
    
    best = 1000
    for j in range(1,1001):
        cost = j
        for i in range(j+1,1001):
            cost += (math.ceil(i/j)-1)*pancakes[i]
        if cost < best:
            best = cost
    out += str(best)+"\n"
    
print(out)
outfile.write(out)
    
outfile.close()
infile.close()