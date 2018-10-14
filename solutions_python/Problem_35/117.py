MAX_HEIGHT = 10000
T = int(raw_input())
char = ''
def dfs(used,grid,x,y):
    global char
    if used[y][x] != None: return used[y][x]
    move = [(0,-1),(-1,0),(1,0),(0,1)]
    values =  [grid[y+y1][x+x1] for (x1,y1) in move]
    small = min(values)
    if small >= grid[y][x]:
        used[y][x] = char
        char = chr(ord(char) + 1)
        return used[y][x]
    for i in xrange(len(move)):
        if small == values[i]:
            flow = move[i]
            break
    p =  dfs(used,grid,x+flow[0],y+flow[1])
    used[y][x] = p 
    return p    
for i in xrange(T):
    char = 'a'
    H,W = map(int,raw_input().split())
    grid = [[MAX_HEIGHT+1 for p in xrange(W+2)  ] for j in xrange(H+2) ] 
    for k in xrange(H):
        li = raw_input().split(' ')
        for j in xrange(W):
            grid[k+1][j+1] = int(li[j])
    used = [[None for p in xrange(W+2)] for j in xrange(H+2) ]
    for y in xrange(1,H+1):
        for x in xrange(1,W+1):
            if used[y][x] == None:
                dfs(used,grid,x,y)
    used = [[ used[J][K] for K in xrange(1,W+1)] for J in xrange(1,H+1)]       
    print "Case #%d:\n%s" % (i+1,'\n'.join([' '.join([k for k in line]) for line in used ]))
