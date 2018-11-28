'''
Created on Apr 13, 2013

@author: FENNERK
'''

f=open('B-small-attempt0.in','r')
cases=int(f.readline())

def check(grid,M,N):
    
    for a in range(0, N):
        for b in range(0,M):
            grid[a][b]=int(grid[a][b])
    
           
    possible="YES"
    minVal=min(min(grid))

    for n in range(0,N):
        for m in range(0,M):
            
            if grid[n][m]==minVal or grid[n][m]==101+minVal:
                row=1
                col=1
               
                for p in range(0, M):
                    if grid[n][p]!=minVal and grid[n][p]!=101+minVal:
                        
                        row=0
                        break
                if row==1:
                    for p in range(0,M):
                        grid[n][p]=101+minVal
                     
                                            
                for q in range(0,N):
                    if grid[q][m]!=minVal and grid[q][m]!=101+minVal:
                        col=0
                        break
                 
                if col==1:
                    for q in range(0,N):
                        grid[q][m]=101+minVal
                
            
                if (row+col)==0:
                    possible="NO"
                    break  
    
    minVal=min(min(grid))
    for y in range(0, M):
        for z in range(0,N):
            if grid[z][y]>100:
                grid[z][y]=minVal
    
    sum=0
    for v in range(0,M):
        for w in range(0,N):
            sum=sum+grid[w][v]
            
    sum=sum/M/N
    
    if sum!=minVal:
        possible=check(grid,M,N)
    
    
    return possible

for i in range(0, cases):
    size=f.readline()
    temp=size.split()
    N=int(temp[0])
    M=int(temp[1])
    grid=[]
    for j in range(0, N):
        grid.append(f.readline().split())
    
        
    poss=check(grid,M,N)
    print "Case #" + str(i+1) +": "+poss
            
    
