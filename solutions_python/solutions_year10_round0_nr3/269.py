from sys import stdin
from collections import deque


T = int(stdin.readline())

for i in xrange(0, T):
    line = stdin.readline()
    nums = line.split()
    R = int(nums[0])
    k = int(nums[1])
    N = int(nums[2])
    
    line = stdin.readline()
    queue = line.split()
    queue = [int(x) for x in queue]
    queue = deque(queue)
    
    earn = 0
    for j in xrange(0, R):
        seats = 0
        newque = deque()
        while len(queue) > 0:
            cur = queue.popleft()  
            if seats + cur <= k:
                seats += cur
                newque.append(cur)
            else:
                queue.appendleft(cur)
                break
        earn += seats
        queue.extend(newque)
        
    
    print "Case #" + str(i + 1) + ":", earn  
