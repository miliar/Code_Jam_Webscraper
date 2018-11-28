import sys
import time

def read(f = int): return f(input())
def readlist(f = int): return list(map(f, input().split()))
def printd(msg): print(msg); print(msg, file=sys.stderr)

def solve():
    S,K = readlist(str)
    S,K = list(S),int(K)
    def flip(n):
        for i in range(K):
            S[n+i] = '-' if S[n+i] == '+' else '+'
            
    ans = 0
    for i in range(0,len(S)-K+1):
        if S[i] == '-':
            flip(i)
            ans += 1
    return ans if all(S[i] == '+' for i in range(len(S))) else 'IMPOSSIBLE'

start = time.clock()
for t in range(read()):
    printd('Case #{}: {}'.format(t+1, solve()))
print(time.clock()-start, file=sys.stderr)
