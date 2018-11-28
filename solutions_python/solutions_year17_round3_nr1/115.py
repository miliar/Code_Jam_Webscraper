import sys, math
import heapq

def area(r):
    return r ** 2 * math.pi

def sides(r, t):
    return 2 * r * t * math.pi

T = int(sys.stdin.readline())

for t in range(T):
    N, K = map(int, sys.stdin.readline().split())
    pc = [None] * N
    for i in range(N):
        r, h = map(float, sys.stdin.readline().split())
        pc[i] = (r, h)

    smallest = []
    pc.sort(key=lambda x: (x[0], -x[1]))
    curSA = 0 
    curRad = 0
    included = [False] * N

    for i in range(K):
        side = sides(pc[i][0], pc[i][1])
        curSA += side
        curRad = pc[i][0]
        heapq.heappush(smallest, [side, i])

        included[i] = True
    

    for i in range(K, N, 1):
        side = sides(pc[i][0], pc[i][1])
        if side > smallest[0][0]:
            smallSA = heapq.heappop(smallest)
            heapq.heappush(smallest, [side, i])
            curRad = pc[i][0]
            curSA += side - smallSA[0]
            included[i] = True
            included[smallSA[1]] = False

    smallestSide = smallest[0][0]
    
    for i in range(N):
        if pc[i][0] > curRad and not included[i]:
            delta = area(pc[i][0]) - area(curRad) + (sides(pc[i][0], pc[i][1]) - smallestSide)
            if delta > 0:
                curRad = pc[i][0]
                curSA += sides(pc[i][0], pc[i][1]) - smallestSide
                smallestSide = sides(pc[i][0], pc[i][1])
    
    curSA += area(curRad)
            
    print("Case #" + str(t + 1) + ": " + "{0:.8f}".format(curSA))
        
        
        

    


        



        



