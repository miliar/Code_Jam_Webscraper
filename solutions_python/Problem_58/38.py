import sys, os

answers = {}

def winning(A, B):
    if A == B: return False
    if A < B:
        B,A = A,B
    if answers.has_key((A,B)): return answers[(A,B)]
    if A==0 or B == 0: return True
    if A-B < B:
        res = not winning(A%B, B)
        answers[(A,B)] = res
        return res
    else:
        res = (not winning(A%B+B, B)) or (not winning(A%B,B))
        answers[(A,B)] = res
        return res
    
fd = open(sys.argv[1], "r")
num = int(fd.readline())
for i in range(num):
    inp = fd.readline()
    inp = inp.replace("\n", "")
    inp = inp.split(" ")
    a1 = int(inp[0])
    a2 = int(inp[1])
    b1 = int(inp[2])
    b2 = int(inp[3])
    count = 0
    for a in range(a1, a2+1):
        for b in range(b1, b2+1):
            if (winning(a,b)): count += 1
    print "Case #%d: %d" % (i+1, count)
    