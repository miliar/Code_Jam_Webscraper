import sys, string
from copy import copy, deepcopy

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

def full(R,C):
    A = []
    for i in range(R):
        A.append(['*'] * C)
    return A

def dump(A):
    R = len(A)
    C = len(A[0])
    for i in range(R):
        s = ""
        for j in range(C):
            s += A[i][j]
        print s
    #~ print

def clean(A):
    A = deepcopy(A)
    R = len(A)
    C = len(A[0])
    for i in range(R):
        for j in range(C):
            if A[i][j] != '*':
                A[i][j] = '.'
    return A

def count(A,printsol):
    A = deepcopy(A)
    R = len(A)
    C = len(A[0])
    for i in range(R):
        for j in range(C):
            if A[i][j] == '.':
                for ii in range(i-1,i+2):
                    for jj in range(j-1,j+2):
                        if ii >= 0 and jj >= 0 and ii < R and jj < C:
                            if A[ii][jj] == '*':
                                A[ii][jj] = ','
    n = 0
    for i in range(R):
        for j in range(C):
            if A[i][j] != '*':
                n += 1

    if printsol:
        A = clean(A)
        A[printsol[0]][printsol[1]] = 'c'
        dump(A)
        return A
        
    return n

def expand(A):
    A = deepcopy(A)
    R = len(A)
    C = len(A[0])
    for i in range(R):
        for j in range(C):
            if A[i][j] == '.':
                for ii,jj in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                    if ii >= 0 and jj >= 0 and ii < R and jj < C:
                            if A[ii][jj] == '*':
                                X = deepcopy(A)
                                X[ii][jj] = '.'
                                yield X

def click(A,i,j):
    R = len(A)
    C = len(A[0])

    n = 0
    for ii in range(i-1,i+2):
        for jj in range(j-1,j+2):
            if ii >= 0 and jj >= 0 and ii < R and jj < C:
                if A[ii][jj] == '*':
                    n += 1
    A[i][j] = "%d" % n
    if n == 0:
        for ii in range(i-1,i+2):
            for jj in range(j-1,j+2):
                if ii >= 0 and jj >= 0 and ii < R and jj < C:
                    if A[ii][jj] == '.':
                        click(A,ii,jj)

def is_solved(A):
    R = len(A)
    C = len(A[0])
    for i in range(R):
        for j in range(C):
            if A[i][j] == '.':
                return False
    return True

def solve(R,C,M):
    Q = [full(R,C)]
    Q[0][0][0] = '.'
    i = 0
    
    if 0:
        ex = list(expand(Q[0]))
        ex = list(expand(ex[0]))
        for e in ex:
            dump(e)
            print
        return

    if R*C-M == 1:
        Q[0][0][0] = 'c'
        dump(Q[0])
        return
    
    while i < len(Q):
        c = Q[i]
        #~ dump(c)
        #~ print
        cnt = count(c,0)
        if cnt == R*C - M:
            sol = count(c,(0,0))
            click(sol,0,0)
            #~ print is_solved(sol)
            #~ dump(sol)
            return
        
        if cnt < R*C - M:
            for d in expand(c):
                if d not in Q:
                    Q.append(d)
        i += 1







    Q = [full(R,C)]
    Q[0][R/2][C/2] = '.'
    i = 0
    
    if R*C-M == 1:
        Q[0][R/2][C/2] = 'c'
        dump(Q[0])
        return
    
    while i < len(Q):
        c = Q[i]
        
        cnt = count(c,0)
        if cnt == R*C - M:
            sol = count(c,(R/2,C/2))
            click(sol,R/2,C/2)
            #~ print is_solved(sol)
            #~ dump(sol)
            return

        if cnt < R*C - M:
            for d in expand(c):
                if d not in Q:
                    Q.append(d)
        i += 1
    
    print "Impossible"

T = readint()

for t in range(T):
    
    R,C,M = readlist()
    print >> sys.stderr, "Case #%d:" % (t+1)
    print "Case #%d:" % (t+1)
    solve(R,C,M)
