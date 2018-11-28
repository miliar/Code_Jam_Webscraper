
# coding: utf-8

# In[272]:

#mode = 'practice'
#mode = 'small'
mode = 'large'
problem = 'A'
attempt = '0'


# In[273]:

import numpy as np
if mode == 'practice':
    infile = 'input.txt'
    outfile = 'output.txt'
if mode == 'small':
    infile = problem+'-small-attempt'+attempt+'.in'
    outfile = problem+'-small.out'
if mode == 'large':
    infile = problem+'-large'+'.in'
    outfile = problem+'-large.out'
f = open(infile, 'r')
lines = f.readlines()
f.close()
cases = int(lines[0].rstrip())
outputfile = open(outfile, 'w')
pos = 0


# In[268]:

def solve(R,C,grid):
    done = []
    out = "\n"
    for i in range(R):
        for j in range(C):
            if not(grid[i][j]=='?') and not(grid[i][j] in done):
                up,left,bottom,right = find_block(R,C,grid,i,j)
                done.append(grid[i][j])
                for k in range(up-bottom+1):
                    for l in range(right-left+1):
                        grid[bottom+k][left+l] = grid[i][j]
    for i in range(R):
        for j in range(C):
            out=out+grid[i][j]
        if i < R-1:
            out=out+"\n"
    return out


# In[269]:

def find_block(R,C,grid,i,j):
    leftfind = 0
    rightfind = C-1
    upfind = R-1
    bottomfind = 0
    found = 0
    for k in range(j):
        if not(grid[i][j-k-1]=='?') and found == 0:
            leftfind = j-k
            found = 1
    found = 0
    for k in range(C-j-1):
        if not(grid[i][j+k+1]=='?') and found == 0:
            rightfind = j+k
            found = 1
    found = 0
    for k in range(i):
        for l in range(rightfind-leftfind+1):
            if not(grid[i-k-1][leftfind+l] == '?') and found == 0:
                found = 1
                bottomfind = i-k
    found = 0
    for k in range(R-i-1):
        for l in range(rightfind-leftfind+1):
            if not(grid[i+k+1][leftfind+l] == '?') and found == 0:
                found = 1
                upfind = i+k
    return upfind, leftfind, bottomfind, rightfind
            


# In[270]:

for i in range(cases):
    pos = pos+1
    grid = []
    dims = lines[pos].rstrip().split(" ")
    R = int(dims[0])
    C = int(dims[1])
    for j in range(R):
        pos = pos+1
        cols = []
        for k in range(C):
            cols.append(lines[pos][k])
        grid.append(cols)
    out = "CASE #" + str(i+1) + ": " + solve(R,C,grid)
    outputfile.write(out)
    outputfile.write("\n")


# In[271]:

outputfile.close()


# In[ ]:




# In[ ]:



