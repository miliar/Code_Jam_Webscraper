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
            

@codejam
def problem2(f):
    return 0

@codejam
def problem3(f):
    return 0

problem1()
