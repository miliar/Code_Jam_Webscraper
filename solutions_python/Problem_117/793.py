'''
Created on Apr 12, 2013

@author: herman
'''

infile = open("small_input.txt","r")
outfile = open("small_output.txt","w")

trials = int(infile.readline())

def possible(lawn,N,M):
    row_maxs = [max(lawn[i]) for i in xrange(N)]
    col_maxs = [0 for y in xrange(M)]
    for j in xrange(M):
        col = [lawn[i][j] for i in xrange(N)]
        col_maxs[j] = max(col)
        
    is_poss = True
    for i in xrange(N):
        for j in xrange(M):
            is_poss = is_poss and (lawn[i][j] == row_maxs[i] or lawn[i][j] == col_maxs[j])
    return is_poss
    

for i in xrange(trials):
    dim = [int(x) for x in infile.readline().split()]
    N = dim[0]
    M = dim[1]
    lawn = [[] for x in xrange(N)]
    for j in xrange(N):
        lawn[j] = [int(x) for x in infile.readline().split()]
    
    if possible(lawn,N,M):
        result = 'YES'
    else:
        result = 'NO'
    s = "Case #%d: %s\n" %(i+1,result)
    outfile.write(s)
    print s
    
infile.close()
outfile.close()