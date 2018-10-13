import sys

INPUT_FILE_PATH = "B-small-attempt0.in"
OUTPUT_FILE_PATH = "out.txt"

f = open(INPUT_FILE_PATH, "r")
of = open(OUTPUT_FILE_PATH,'w')
# -------------------------------------------------
def scout(y,x,v):
    Obstacle = 0
    #check in the row
    for i in range(0, M):
        if A[y][i] > v:
            Obstacle += 1
            break
    #check in the column
    for j in range(0, N):
        if A[j][x] > v:
            Obstacle += 1
            break
    if (Obstacle == 2): return False
    return True
    
def solve():
    pos = {}
    for i in range(0,N):
        for j in range(0,M):
            if A[i][j] in pos:
                pos[A[i][j]].append([i,j])
            else:
                pos[A[i][j]] = [[i,j]]
    #print pos
    
    keys = pos.keys()
    keys.sort()
    keys.reverse()
    
    #print keys

    for k in keys:
        for p in pos[k]:
            if not scout(p[0],p[1],k):
                return "NO"
    return "YES"
            
        

# -------------------------------------------------
T = int(f.readline().strip())

for C in range(1,T+1):
    tmp = f.readline().strip().split(' ')

    # problem = 
    N = int(tmp[0])
    M = int(tmp[1])   
    A = []
    for i in range(0,N):
        tmp = f.readline().strip().split(' ')
        A.append(tmp)
    #print "Case #"+str(C)+": "+solve()
    of.write("Case #"+str(C)+": "+solve()+"\n")
print "DONE"
    
            

# -------------------------------------------------


