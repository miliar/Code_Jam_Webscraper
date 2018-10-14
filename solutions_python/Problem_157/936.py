import sys, string
from copy import copy, deepcopy
import gmpy
import time

import sys
sys.setrecursionlimit(1000000)

def readlist():
	return [int(x) for x in sys.stdin.readline().strip().split(" ")]

def readbinlist():
	return [int(x,2) for x in sys.stdin.readline().strip().split(" ")]

def readint():
	return int(sys.stdin.readline())

T = readint()

def quatmul(a,b):

    if a[0] == '-':
        q = quatmul(a[1], b)
        return q[1:] if q[0] == '-' else "-" + q

    if b[0] == '-':
        q = quatmul(a, b[1])
        return q[1:] if q[0] == '-' else "-" + q
    
    if a == '1':
        return b
    
    if b == '1':
        return a

    if a == 'i':
        return "-1" if b == 'i' else "k" if b == 'j' else "-j"

    if a == 'j':
        return "-k" if b == 'i' else "-1" if b == 'j' else "i"

    if a == 'k':
        return "j" if b == 'i' else "-i" if b == 'j' else "-1"

msg = ""
L = 0
eval_left = []
eval_right = []

def precompute():
    acc = "1"
    for i in range(L):
        acc = quatmul(acc, msg[i])
        eval_left.append(acc)
        eval_right.append(acc)
    
    acc = "1"
    for i in range(L-1,-1,-1):
        acc = quatmul(msg[i], acc)
        eval_right[i] = acc
    
    #~ print eval_left
    #~ print eval_right

def eval(a,b):
    if a == 0:
        return eval_left[b-1]
    if b == L:
        return eval_right[a]
    
    A = eval_left[a-1]
    B = eval_right[b]
    C = eval_left[-1]
    
    for x in ['1', 'i', 'j', 'k', '-1', '-i', '-j', '-k']:
        if quatmul(quatmul(A,x),B) == C:
            return x

for t in range(T):
    L, X = readlist()
    msg = sys.stdin.readline()[:L] * X
    L = L * X
    eval_left = []
    eval_right = []
    
    print >> sys.stderr, "Solving case #%d..." % (t+1)
    print ("Case #%d:" % (t+1)),

    ans = "NO"
    
    if L <= 2:
        print ans
        continue
    
    precompute()
    #~ if L == 12:
        #~ print msg[0:3], eval(0,3)
        #~ print msg[3:6], eval(3,6)
        #~ print msg[6:], eval(6,L)
    
    for i in range(1,L):
        if i > 500:
            break
        if eval(0,i) == 'i':
            for j in range(i+1,L):
                if eval(j,L) == 'k' and eval(i,j) == 'j':
                    ans = "YES"
                    #~ print msg[:i], msg[i:j], msg[j:]
                    break
        if ans == "YES":
            break
    print ans
