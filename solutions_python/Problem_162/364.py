import sys
import heapq as hq

counts = {}

lastnum = 1000000
h = []
hq.heappush(h, (1,1))
while len(counts) < lastnum:
    #print h[0],len(counts)
    steps,i = hq.heappop(h)
    if (i not in counts) or steps < counts[i]:
        counts[i] = steps
        hq.heappush(h,(steps+1,i+1))
        j = int(str(i)[::-1])
        hq.heappush(h,(steps+1,j))
#for x in range(1,1000001):
#    print x, counts[x]
#sys.exit()




f = open(sys.argv[1])
f.readline()
t = 1
for l in f:
    n = int(l)
    output = counts[n]
    print "Case #{}: {}".format(t,output)
    t += 1
f.close()
