import os,sys
sys.setrecursionlimit(10000)
f = open('./input.txt',"r")
output = open('./output.txt',"w")
def out(t,sol):
    s = "Case #" + str(t+1) + ": " + str(sol)
    print(s)
    output.write(s + "\n")
T = int(f.readline())

def deal(s, K, x):
    if 0 not in s:
        return x
    i = s.index(0)
    if i > l - K:
        return -1
    for j in range(i, i+K):
        if s[j] == 0:
            s[j] = 1
        else:
            s[j] = 0
    return deal(s, K, x+1)

for t in range(0,T):
    S,K = f.readline().split()
    K = int(K)
    l = len(S)
    s = [1]*l
    for i in range(l):
        if S[i] == '-':
            s[i] = 0
    x = deal(s, K, 0)
    if x < 0:
        out(t,"IMPOSSIBLE")
    else:
        out(t,x)
output.close()




