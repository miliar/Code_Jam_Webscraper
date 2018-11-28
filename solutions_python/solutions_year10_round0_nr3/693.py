#! /usr/bin/env python

from collections import deque

file = open("C-small.in", "r")

header = file.readline();

testCases = int(header)

for i in range(testCases):
    header = file.readline()
    header = header.split()
    R = int(header[0])
    k = int(header[1])
    N = int(header[2])
    
    line = file.readline().split()
    queue = deque()
    
    for l in line:
        queue.append(int(l))
    
    euros = 0
    for j in range(R):
        pointer = 0
        more = 1
        count = 0
        car = deque()
        
        while (more and len(queue) > 0):
            p = queue.popleft()
            if (p + count <= k):
                car.append(p)
                count = count + p
            else:
                queue.appendleft(p)
                more = 0;

        while (len(car) > 0):
            p = car.popleft()
            euros = euros + p
            queue.append(p)
        
                
    print "Case #" + str((i + 1)) + ": " + str(euros)
            
    
