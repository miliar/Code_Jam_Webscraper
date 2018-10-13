#!/usr/bin/python3

def stallrec(state, K):
    M = max(state)
    mm = state[M]
    if K < mm: return M
    x = M//2
    y = (M-1)//2
    try: state[x] += mm
    except(KeyError): state[x] = mm
    try: state[y] += mm
    except(KeyError): state[y] = mm
    del state[M]
    return stallrec(state, K-mm)

def stall(N, K):
    livre = stallrec({N: 1}, K-1)
    return livre//2, (livre-1)//2
 
if __name__ == "__main__":
    T = int(input())
    for case in range(1, T+1):
        line = input().split(' ')
        N = int(line[0])
        K = int(line[1])
        r, s = stall(N, K)
        print("Case #%d: %d %d"%(case, r, s))
