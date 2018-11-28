'''
Created on Apr 8, 2013

@author: kon
'''
import template
import numpy as np

def possible(inp, n, k):
    ans = True
    max_col = [0]*k
    max_row = [0]*n
    for i in range(k):
        max_col[i] = max(inp[:,i])
    for i in range(n):
        max_row[i] = max(inp[i,:])
    for i in range(n):
        for j in range(k):
            if (inp[i,j] != min(max_row[i], max_col[j])):
                ans = False
                break
    return ans

def solve(f):
    T = int(f.readline())
    res = []
    for _ in range(T):
        N, K = map(int,f.readline().split())
        inp = np.ones((N,K), dtype=np.int)
        for i in range(N):
            heights = map(int,f.readline().split())
            for j,h in enumerate(heights):
                inp[i,j] = h
        if possible(inp, N, K):
            res.append('YES')
        else:
            res.append('NO')

    return res

if __name__ == '__main__':
    template.solve("B-large.in", solve)