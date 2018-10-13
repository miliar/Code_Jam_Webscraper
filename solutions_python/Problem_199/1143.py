from sys import *

def solve(S,K,ind,count):
    if ind >= len(S):
        return count
    elif S[ind]==1:
        return solve(S,K,ind+1,count)
    elif S[ind]==0 and ind > len(S)-K:
        return "IMPOSSIBLE"
    else:
        S[ind:ind+K] = [1-x for x in S[ind:ind+K]]
        return solve(S,K,ind+1,count+1)

setrecursionlimit(5000)

f = open("A-large.in","r")
g = open("output.txt","w")

T = int(f.readline())

for i in range(1,T+1):
    [S,K] = f.readline().split()
    K = int(K)
    a={'-':0,'+':1}
    pancakes = [a[j] for j in S]

    # Solve
    ans = solve(pancakes,K,0,0)

    g.write("Case #{}: {}\n".format(i,ans))

f.close()
g.close()
