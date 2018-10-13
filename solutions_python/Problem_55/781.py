from collections import deque

cases = input()
for c in range(cases):
    R, k, N = map(int, raw_input().split())
    queue = map(int, raw_input().split())

    total = 0
    for ride in range(R):
        size = 0
        count = 0
        for i in range(len(queue)):
            if (size + queue[i] <= k):
                size += queue[i]
                count += 1
            else:
                break

        total += size
        queue = queue[count:len(queue)] + queue[0:count]

    print "Case #" + str(c+1) + ":", total
    
