#save the universe

def solve(querry, engn):
    plan = [[0 for y in xrange(engn)] for x in xrange(len(querry))]
    dist = 0
    for x in xrange(len(plan)):
        if x==0:
            dist = 0
            fromnodes = range(engn)
        else:
            dist = min(plan[x-1])
            fromnodes = [n for n in xrange(engn) if plan[x-1][n]==dist]
        for y in xrange(engn):
            if y in fromnodes:
                plan[x][y] = dist
            else:
                plan[x][y] = dist + 1
        plan[x][querry[x]] = 1e12
    if len(plan) > 1:
        dist = min(plan[len(plan)-1])
    else:
        dist = 0
    print 'plan'
    for p in plan:
        print p
    return dist

#loading input
f = open('A-large.in')
fout = open('output.txt','w')
N = int(f.readline())
for en in xrange(N):
    #read data
    S = int(f.readline())
    engines = {}
    engn = 0
    for sn in xrange(S):
        engines[f.readline()[:-1]] = engn
        engn += 1
    querry = []
    Q = int(f.readline())
    for qn in xrange(Q):
        qs = f.readline()[:-1]
        if qs in engines:
            querry.append(engines[qs])
    print querry    
    n = solve(querry, engn)
    fout.write( 'Case #%d: %d\n' % (en+1, n) )
f.close()
fout.close()
    
    
