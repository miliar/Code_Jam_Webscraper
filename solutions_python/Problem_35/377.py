from numpy import *
import sys

DIRS = [ (-1,0), (0, -1), (0, 1), (1, 0) ]

def checkBounds(p):
    return p[0] >= 0 and p[1] >= 0 and p[0] < H and p[1] < W
    
    
def flowDir(p):
    min = map[p]
    minDir = (0,0)
    
    for i in DIRS:
        np = ( p[0] + i[0], p[1] + i[1] )
        
        if checkBounds(np) and map[np] < min:
            min = map[np]
            minDir = i
    return minDir

def sink(p):
    return dirs[p][0] == 0 and dirs[p][1] == 0

def flow(p):
    global labelCount
    if (labels[p] != 0):
        return;
    
    path = []
    
    while (not sink(p)):
        path.append(p)
        v = dirs[p]
        p = (p[0] + v[0], p[1] + v[1])
        
    if (labels[p]==0):
        labels[p] = labelCount
        label = labelCount
        labelCount = labelCount+1
    else:
        label = labels[p]
        
    for i in path:
        labels[i] = label
        
infile = open ("in1", "r")
Nmaps = int(infile.readline())

for N in range(1,Nmaps+1):
    print "Case #" + str(N) + ":"
    Hs,Ws = infile.readline().split()
    H,W = int(Hs), int(Ws)

    map = zeros ((H,W), dtype=int16)
    labels = zeros ((H,W), dtype=int16)
    
    for i in range(0,H):
        heights = infile.readline().split()
        for j in range(0,W):
            map[i,j] = int (heights[j])
    
    dirs = zeros ( (H,W,2), dtype=int16 )
    
    for i in range(0,H):
        for j in range(0,W):
            dirs[i,j] = flowDir( (i,j) )
            
    labelCount = 1
    
    for i in range(0,H):
       for j in range(0,W):
           flow( (i,j) )
           
    for i in range(0,H):
       for j in range(0,W):
           if (j>0):
               sys.stdout.write(" ")
           sys.stdout.write(chr(labels[i,j]+96))
       print ""        