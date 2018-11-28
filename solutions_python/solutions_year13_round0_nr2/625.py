import time
'''
class node:
    def __init__:
        self.satisfied = False
        self.height = 100
        self.goal = 100
    def setHeight(h):
        if h < self.goal:
            return -1
        self.height = h
        if h == self.goal
            self.satisfied = True
            return 1
        return 0
'''
def heighestNode(grid,x,xInc,y,yInc,n,m):
    maxG = 0
    while x < n and y < m:
        if grid[x][y] > maxG:
            maxG = grid[x][y]
        x += xInc
        y += yInc
    return maxG

def recurseLine(grid,x,y,n,m,h):
    if y == m:
        return True
    if grid[x][y] < h:
        if heighestNode(grid,0,1,y,0,n,m) > grid[x][y]:
            return False
    return recurseLine(grid,x,y +1,n,m,h)

t = time.clock()
f = open("ProblemB-Small.txt")
f.readline()

outFile = open("ProblemB-Out.txt",'w')
c = 0
while True:
    c+=1
    counts = f.readline()[:-1]
    
    if len(counts) == 0:
        break
    countsP = counts.split(' ')
    n = int(countsP[0])
    m = int(countsP[1])
    grid = []
    for i in range(n):
        grid.append(f.readline()[:-1].split(' '))
#    print grid

    message = "YES"
    for i in range(n):
        h = heighestNode(grid,i,0,0,1,n,m)
        if not recurseLine(grid,i,0,n,m,h):
            message = "NO"
            break

    outFile.write("Case #{0}: {1}\n".format(c, message))
    print "Case #{0}: {1}".format(c, message)
print time.clock() - t
f.close()
outFile.close()
