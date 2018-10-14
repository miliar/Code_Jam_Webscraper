
from collections import defaultdict as ddic
def solve(R,C,A):
    G = ddic(list)
    # Rows
    for i in xrange(R):
        tmp = []
        for j in xrange(C):
            if A[i][j] != '.': tmp.append((i,j))
        tmplen = len(tmp)
        if tmplen > 1:
            G[tmp[0]].append('>')
            G[tmp[tmplen-1]].append('<')
            for i in xrange(1,tmplen-1):
                G[tmp[i]].append('>')
                G[tmp[i]].append('<')
        else:
            pass

    #Columns
    for j in xrange(C):
        tmp = []
        
        for i in xrange(R):
            if A[i][j] != '.': tmp.append((i,j))
        tmplen = len(tmp)
        if tmplen > 1:
            G[tmp[0]].append('v')
            G[tmp[tmplen-1]].append('^')
            for i in xrange(1,tmplen-1):
                G[tmp[i]].append('v')
                G[tmp[i]].append('^')
        else:
            pass
    #Now G is a list of valid
    ans = 0

    for i in xrange(R):
        for j in xrange(C):
            if A[i][j]  != '.':
                if G[(i,j)]:
                    if (A[i][j] not in G[(i,j)]): ans += 1
                else:
                    return "IMPOSSIBLE"
    return ans

########
fo = open('out.txt','w')
with open('in.txt','r') as fi:
    rr = lambda: fi.readline().strip()
    rrI = lambda: int(rr())
    rrM = lambda: map(int,rr().split())
    for tc in xrange(rrI()):
        R,C = rrM()
        A = [rr() for i in xrange(R)]
        zetaans = solve(R,C,A)
        zeta = "Case #%i: "%(tc+1) + str(zetaans)
        print zeta
        fo.write(zeta+'\n')
fo.close()
