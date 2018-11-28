#!/usr/bin/env python3

inf = float('inf')
read_ints = lambda : list(map(int, input().split()))

def solve(N):
    L = list(str(N))
    left = 0
    for i in range(len(L)-1):
        if L[i] < L[i+1]:
            left = i + 1
        elif L[i] > L[i+1]:
            if L[i] == '1':
                L = ['9'] * (len(L)-1)
            else:
                L[left] = chr(ord(L[i])-1)
                L[left+1:] = ['9'] * (len(L) - left - 1)
            break
    return int(''.join(L))

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        print('Case #%d: %d' % (t, solve(N)))