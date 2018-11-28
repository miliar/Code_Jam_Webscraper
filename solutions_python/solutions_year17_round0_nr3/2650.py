import sys
import heapq

with open(sys.argv[1]) as infile:
    numcases = int(next(infile))

    for casenum in range(1,numcases+1):
        lArr = next(infile).rstrip().split()
        n = int(lArr[0])
        k = int(lArr[1])
        
        heap = []
        heapq.heappush(heap,-1*n)

        min = 0
        max = 0
        for _ in range(k):
            largest_size = heapq.heappop(heap)
            if largest_size % 2 == 1:
                split = int(largest_size / 2)
                heapq.heappush(heap,split)
                heapq.heappush(heap,split)
            else:
                split = int(largest_size / 2)
                heapq.heappush(heap,split)
                heapq.heappush(heap,split+1) #plus 1 because neg
            
        if largest_size % 2 == 1:
            min = -1*split
            max = -1*split
        else:
            min = (-1*split)-1
            max = (-1*split)

        print("Case #{}: {} {}".format(casenum,max,min))
        
        
