#!/usr/bin/python
import sys
def draw(a, b, H, W):
    # N, W, S, E
    link = [[ [0,0,0,0] for i in range(0,W)] for j in range(0,H)]
    direction = [[-1,0], [0,-1], [0,1], [1,0]]    
    
    for i in range(0,H):
        for j in range(0,W):
            low = (i,j)
            lowd = -1
            
            # find the lowest neighbour
            tempd = 0
            for d in range(0,4):
                newi = i + direction[d][0]
                newj = j + direction[d][1]
                
                if newi>=0 and newi<H and newj>=0 and newj<W:
#                    if i==2 and j==0:
#                        print i, j, a[i][j], newi, newj, a[newi][newj]
                                            
                    if a[newi][newj] < a[low[0]][low[1]]:
                        low = (newi, newj)
                        lowd = tempd
                tempd += 1
                
            # if found
            if lowd != -1:
                link[i][j][lowd] = 1
                r_lowd = (3-lowd)
                link[low[0]][low[1]][r_lowd] = 1
    
    b = [[' ' for i in range(0, 2*W-1)] for j in range(0, 2*H-1)]

    for i in range(0,H):
        for j in range(0,W):
            b[2*i][2*j] = 0
            for k in range(0,4):
                if link[i][j][k]:
                    if k==0 or k==2:
                        conj = '*'
                    else:
                        conj = '*'
                    b[2*i+direction[k][0]][2*j+direction[k][1]] = conj

    
#    for i in range(0, 2*H-1):
#        s = ""
#        for j in range(0, 2*W-1):
#            s += "%s " % (b[i][j])   
#        print s

    def propagate(i,j, char):
        if c[i][j] != '*':
            return
        c[i][j] = char
        for d in range(0,4):
            if link[i][j][d]:
                propagate(i+direction[d][0], j+direction[d][1], char)
    
    c = [['*' for i in range(0, 2*W-1)] for j in range(0, 2*H-1)]
    char = 'a'
    for i in range(0,H):
        for j in range(0,W):
            if c[i][j] == '*':
                propagate(i,j, char)
                char = chr(ord(char)+1)
        
    for i in range(0,H):
        for j in range(0,W):
            print c[i][j],
        print
        
    
infile = "B-large.in"
fin = open(infile)

#outfile = "B-small.out"
#fout = open(outfile, "w+")

num = fin.readline()

for k in range(0,int(num)):
    temp = fin.readline().split()
    H = int(temp[0])
    W = int(temp[1])
    a = []
    b = []
    for i in range(0, H):
        a.append([int(j) for j in fin.readline().split()])
        b.append([-1 for j in a[i]])
    
    print "Case #%d:" % (k+1)
    draw(a,b,H,W)
