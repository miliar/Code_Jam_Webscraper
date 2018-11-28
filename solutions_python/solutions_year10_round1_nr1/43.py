USE_PSYCHO = True
#USE_PSYCHO = False

if USE_PSYCHO:
    import psyco
    psyco.full()


def g(arr, N, x, y):
    if (x >= 0 and x < N and y>=0 and y<N):
        return arr[x,y]
    else:
        return 0



def solve(filecontent):
    lines = filecontent.splitlines()
    T = int(lines[0])
    out = []
    lines = lines[1:]
    for tcase in xrange(1,T+1):
        print "tcase is ",tcase
        line1 = lines[0].split(" ")
        N = int(line1[0])
        K = int(line1[1])
        
        import numpy as np
        arr = np.zeros((N,N))

        beforeRot = lines[1:N+1]
        assert(len(beforeRot)==N)

        columns = [x[::-1] for x in beforeRot]
        gravColumns = [x.replace(".","") + "".join(N*'.') for x in columns]

        # fill arr with testcase
        for x in xrange(N):
            for y in xrange(N):
                if gravColumns[x][y] == 'R':
                    arr[x,y] = 1
                if gravColumns[x][y] == 'B':
                    arr[x,y] = 2

        #print "-----"
        #print arr
        
        has = [False, False]
        for color in [1,2]:
            for direc in [(1,0), (0,1), (1,1), (1,-1)]:
                for x in xrange(N):
                    for y in xrange(N):
                        num = 0
                        for l in xrange(K):
                            if g(arr, N, x+l*direc[0], y+l*direc[1]) == color:
                                num += 1
                        if num == K:
                            has[color-1] = True
                    
        tcaseOut = ("Case #%d: " % (tcase,))
        if has == [False,False]:
            s = 'Neither'
        elif has == [True,False]:
            s = 'Red'
        elif has == [False,True]:
            s = 'Blue'
        elif has == [True, True]:
            s = 'Both'
        tcaseOut += s
        out.append(tcaseOut)
        lines = lines[N+1:]
    return "\n".join(out)

f = file("codejam/A-large.in").read()
file("codejam/A-large.out",'w').write(solve(f))
