import heapq

numCases = int(input())
for i in range(1, numCases + 1):
    n, m = [int(x) for x in input().split(' ')]

    distances = [-n]
    heapq.heapify(distances)
    
    for j in range(m):
        currentMax = abs(heapq.heappop(distances))

        if currentMax % 2 == 0:
            left = (currentMax // 2) - 1
            right = (currentMax // 2)
        else:
            left = (currentMax // 2)
            right = (currentMax // 2)
            
            
        if (j == m-1):
            output = "Case #%d: %d %d" % (i, max(left, right), min(left, right))
            print(output)
        
        heapq.heappush(distances, -left)
        heapq.heappush(distances, -right)

        
        
        
