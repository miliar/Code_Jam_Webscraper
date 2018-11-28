#benoni.boy
#Google Code Jam
#13 April 2013
import sys

sys.stdin = open('C:\GCJ\in.txt')
sys.stdout = open('C:\GCJ\out.txt', 'w')

def cuttable(lawn, N, M):
    if N == 1: return True
    if M == 1: return True
    minh = min([min(l) for l in lawn])
    minrow = [minh] * M
    for row in range(N):
        if lawn[row] == minrow:
            del lawn[row]
            return cuttable(lawn, N - 1, M)
    cols = [[lawn[j][i] for j in range(N)] for i in range(M)]
    mincol = [minh] * N
    for col in range(M):
        if cols[col] == mincol:
            del cols[col]
            return cuttable(cols, M - 1, N)

def doCase(c):
    N, M = map(int, input().split())
    lines = [[int(h) for h in input().split()] for i in range(N)]
    cut = 'YES' if cuttable(lines, N, M) else 'NO'
    print('Case #' + str(c + 1) + ': ' + cut)
    

T = eval(input())
for i in range(T):
    doCase(i)

sys.stdin.close()
sys.stdout.close()
