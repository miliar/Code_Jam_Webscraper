import sys

def handle(infile, outfile):
    global engines, queries, mem
    
    n = int(infile.readline())
    engines = [None] * n
    for i in range(n):
        engines[i] = infile.readline()
        
    q = int(infile.readline())
    queries = [None] * q
    for i in range(q):
        queries[i] = infile.readline()
    
    mincost = 100000
    mem = [[None] * q for i in range(n)]
    for i in range(n):
        mincost = min(mincost, process(i, 0))
    
    outfile.write(' %d' % mincost)
    
def process(e, q):
    if q == len(queries): return 0
    if mem[e][q]: return mem[e][q]
    
    mincost = 100000
    if queries[q] != engines[e]:
        return process(e, q + 1)
    else:
        for i in range(len(engines)):
            if i != e:
                mincost = min(mincost, process(i, q) + 1)
                
    mem[e][q] = mincost
    return mincost

if len(sys.argv) != 2: exit()
infile = file(sys.argv[1], 'r')
outfile = file(sys.argv[1] + '.out', 'w')

count = int(infile.readline())
for i in range(count):
    print 'Case #%d' % (i + 1)
    outfile.write('Case #%d:' % (i + 1))
    result = handle(infile, outfile)
    outfile.write('\n')
