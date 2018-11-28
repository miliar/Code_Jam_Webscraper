# coaster question

from sys import argv
from collections import deque

file = open(argv[1])
line1 = file.readline()
testc = int(line1)
outfile = open(argv[1] + ".out", "w")

for testnum in range(1, testc+1):
    line1 = file.readline().split(" ")
    line2 = file.readline().split(" ")
    R = int(line1[0])
    k = int(line1[1]) 
    N = int(line1[2]) 
    queue = deque(map(int, line2))
    print "R=%d, k=%d, N=%d" % (R, k, N), queue    

    total = 0
    for i in range(R):
        onboard = 0
        riding = []
        while len(queue) and onboard + queue[0] <= k:
            g = queue.popleft()
            onboard += g
            riding.append(g)
        total += onboard
        queue.extend(riding) 

    print >>outfile, "Case #%d: %s" % (testnum, total)

