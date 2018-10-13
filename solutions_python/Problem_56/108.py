fin = open('a.txt')
T = int(fin.readline())
fo = open('a.out','w')
for cc in xrange(0,T):
    N,K = [int(i) for i in fin.readline().split()]
    b = []
    
    for x in xrange(0,N):
        l = []
        for c in fin.readline().strip():
            if c == '.':
                continue
            l.append(c)
        b.append("".join(l).rjust(N,'.'))
    s = []
    for i in xrange(0,N+1):
        s.append([])
        for j in xrange(0,N+1):
            s[i].append([])
            for xx in xrange(0,4):
                s[i][j].append(0)
    nn = N - 1
    d = {'R':0,'B':0}
    done = False
    for i in xrange(0,N):
        if done:
            break
        for j in xrange(0,N):
            c = b[i][j]
            t = []
            if c == '.':
                continue
            if i > 0 and b[i-1][j] == c:
                s[i][j][0] = s[i-1][j][0] + 1
            if j > 0 and b[i][j-1] == c:
                s[i][j][1] = s[i][j-1][1] + 1
            if i > 0 and j > 0 and b[i-1][j-1] == c:
                s[i][j][2] = s[i-1][j-1][2] + 1
            if j < nn and i > 0 and b[i-1][j+1] == c:
                s[i][j][3] = s[i-1][j+1][3] + 1
            
            for x in s[i][j]:
                if x >= (K-1):
                    d[c] = 1
            if d['R'] == 1 and d['B'] == 1:
                done = True
                break
  
    fo.write("Case #{0}: ".format(cc+1))
    if done:
        fo.write("Both\n")
    elif d['R'] == 1:
        fo.write("Red\n")
    elif d['B'] == 1:
        fo.write("Blue\n")
    else:
        fo.write("Neither\n")