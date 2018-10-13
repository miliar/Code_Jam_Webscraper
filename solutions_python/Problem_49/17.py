from codejam import *
import math

@codejam
def problem1(f):
    N = read_int(f)
    A = []
    for i in xrange(N):
        s = read_str(f)
        A.append(-1)
        for j in xrange(N-1, -1, -1):
            if s[j] == '1':
                A[i] = j
                break
    m = 0
    #print A
    for n in xrange(N):
        if A[n] > n:
            i = n + 1
            while A[i] > n: i += 1
            t = A[i]
            del A[i]
            A.insert(n, t)
            m += i-n
            #print A, m
    return m
            

def rr(xa, ya, ra, xb, yb, rb):
    return math.sqrt((xa-xb)**2+(ya-yb)**2) + ra + rb
    
@codejam
def problem2(f):
    N = read_int(f)
    X = []
    Y = []
    R = []
    for i in xrange(N):
        x1, y1, r1 = read_list(f)
        X.append(x1)
        Y.append(y1)
        R.append(r1)
    if N < 3: return max(R)
    v1 = max(rr(X[0], Y[0], R[0], X[1], Y[1], R[1]), R[2])
    v2 = max(rr(X[0], Y[0], R[0], X[2], Y[2], R[2]), R[1])
    v3 = max(rr(X[1], Y[1], R[1], X[2], Y[2], R[2]), R[0])
    return 0.5*min(v1, v2, v3)

@codejam
def problem3(f):
    return 0

problem2()
