
# coding: utf-8

# In[15]:

def parse(text):
    T = int(text.next())
    
    for i in range(T):
        R,C = [int(x) for x in text.next().split(" ")]
        
        rows = []
        for j in range(R):
            row = [x for x in text.next().strip()]
            #print row
            rows.append(row)
        
        soln = solveout(R,C,rows)
        
        print "Case #%d: %s" % (i+1, soln)


# In[16]:

TEXT="""5
1 3
-.-
3 4
#.##
#--#
####
2 2
-.
#|
4 3
.|.
-//
.-.
#\/
3 3
/|\
\\/
./#"""


# In[17]:

def solveout(R,C,grid):
    
    
    #check for IMPOSSILBE
    for r in range(R):
        for c in range(C):
            if grid[r][c] == ".":
                
                ok = False
                
                i = c-1
                while i>=0:
                    if grid[r][i] == "#":
                        break
                    if grid[r][i] in "-|":
                        ok = True
                        break
                    i -= 1
                
                i=c+1
                while i <C:
                    if grid[r][i] == "#":
                        break
                    if grid[r][i] in "-|":
                        ok = True
                        break
                    i += 1
                    
                i = r-1
                while i>=0:
                    if grid[i][c] == "#":
                        break
                    if grid[i][c] in "-|":
                        ok = True
                        break
                    i -= 1
                
                i = r+1
                while i <R:
                    if grid[i][c] == "#":
                        break
                    if grid[i][c] in "-|":
                        ok = True
                        break
                    i += 1
                    
                if not ok:
                    return None
    
    
    soln = solve(R,C,grid)
    
    
    if soln:
        return soln
    
    return "IMPOSSIBLE"
    


# In[18]:

def solve(R,C, grid,r=0,c=0):
    #print R,C,grid,r,c
    
    
    
    while r<R:
        while c<C:
            cell = grid[r][c]
            if grid[r][c] in "-|":
                
                #check leftright
                ok = True
                i = c-1
                while i>=0:
                    if grid[r][i] == "#":
                        break
                    if grid[r][i] in "-|":
                        ok = False
                        break
                    i -= 1
                
                i=c+1
                while i <C:
                    if grid[r][i] == "#":
                        break
                    if grid[r][i] in "-|":
                        ok = False
                        break
                    i += 1
                    
                if ok:
                    #print r,c,"-"
                    grid[r][c] = "-"
                    soln = solve(R,C,grid, r,c+1)
                    if soln:
                        return soln
                    
                #check updown
                ok = True
                i = r-1
                while i>=0:
                    if grid[i][c] == "#":
                        break
                    if grid[i][c] in "-|":
                        ok = False
                        break
                    i -= 1
                
                i = r+1
                while i <R:
                    if grid[i][c] == "#":
                        break
                    if grid[i][c] in "-|":
                        ok = False
                        break
                    i += 1
                    
                if ok:
                    #print r,c,"|"
                    grid[r][c] = "|"
                    soln = solve(R,C,grid, r,c+1)
                    if soln:
                        return soln
    
                return None
            c += 1
        c = 0
        r += 1
    
    #got to the end, check if valid!
    for r in range(R):
        for c in range(C):
            if grid[r][c] == ".":
                
                ok = False
                
                i = c-1
                while i>=0:
                    if grid[r][i] == "#":
                        break
                    if grid[r][i] in "-":
                        ok = True
                        break
                    i -= 1
                
                i=c+1
                while i <C:
                    if grid[r][i] == "#":
                        break
                    if grid[r][i] in "-":
                        ok = True
                        break
                    i += 1
                    
                i = r-1
                while i>=0:
                    if grid[i][c] == "#":
                        break
                    if grid[i][c] in "|":
                        ok = True
                        break
                    i -= 1
                
                i = r+1
                while i <R:
                    if grid[i][c] == "#":
                        break
                    if grid[i][c] in "|":
                        ok = True
                        break
                    i += 1
                    
                if not ok:
                    return None
    
    #all good
    soln = "POSSIBLE\n"
    
    soln += "\n".join(["".join(grid[r]) for r in range(R)])
    
    return soln


# In[19]:

#parse(x for x in TEXT.splitlines())


# In[21]:

parse(open("C:\Users\mheik\Downloads\C-small-attempt1.in"))


# In[13]:

TEXT="""1
5 41
#-#|#|#|#-#|#|#|#-#-#|#|#|#-#|#|#|#-#-#-.
-#-#-#|#-#|#-#-#|#-#|#|#-#|#|#|#-#|#|#|#.
#-#|#|#|#-#|#-#|#|#-#|#-#-#-#|#|#-#-#-#|.
|#|#-#|#-#-#|#-#|#|#|#-#-#|#-#-#-#|#-#-#.
#-#|#-#|#-#-#|#-#-#|#|#|#-#-#-#-#-#|#-#-."""


# In[ ]:



