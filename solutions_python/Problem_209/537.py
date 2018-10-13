import math

def solve(N, K, pancakes):
    pancakes = sorted(pancakes, key = lambda pancake: pancake[0])
    stack = []
    totalArea = 0
    count = 0
    
    while(count < K):
        maxArea = 0
        maxI = 0
        radii = max([j[0] for j in stack]+[0])
        for i in range(len(pancakes)):
            area = 0
            if(radii < pancakes[i][0]):
                area = math.pi*(pancakes[i][0]**2-radii**2)
            area += 2*math.pi*pancakes[i][0]*pancakes[i][1]
            if(area > maxArea):
                maxArea = area
                maxI = i
        totalArea += maxArea
        stack.append(pancakes.pop(maxI))
        count += 1
        
    return totalArea

infile = open("A-large (1).in", "r")
outfile = open("A-large (1).out", "w")
T = int(infile.readline())
for i in range(T):
    line = infile.readline().split(" ")
    N = int(line[0])
    K = int(line[1])
    pancakes = [[0, 0] for j in range(N)]
    for j in range(N):
        line = infile.readline().split(" ")
        pancakes[j] = [int(line[0]), int(line[1])]
    outfile.write("Case #"+str(i+1)+": "+str(solve(N, K, pancakes))+"\n")
infile.close()
outfile.close()
