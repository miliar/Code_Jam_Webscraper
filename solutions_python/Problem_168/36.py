#!/usr/bin/python3
# -*- coding: utf-8 -*-

def solve():
    R, C = map(int, input().split())
    m = [input() for _ in range(R)]
    top = [None for _ in range(C)]
    bottom = [None for _ in range(C)]
    left = [None for _ in range(R)]
    right = [None for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if m[i][j] != '.':
                top[j] =i if top[j] is None else min(top[j], i)
                bottom[j] = i if bottom[j] is None else max(bottom[j], i)
                left[i] = j if left[i] is None else min(left[i], j)
                right[i] = j if right[i] is None else max(right[i], j)
    cnt = 0
    for i in range(R):
        for j in range(C):
            if m[i][j] != '.':
                if m[i][j] == '^' and top[j] == i:
                    cnt += 1
                if m[i][j] == 'v' and bottom[j] == i:
                    cnt += 1
                if m[i][j] == '<' and left[i] == j:
                    cnt += 1
                if m[i][j] == '>' and right[i] == j:
                    cnt += 1
                if top[j] == bottom[j] == i and left[i] == right[i] == j:
                    return "IMPOSSIBLE"
    return cnt

if __name__=="__main__":
    T = int(input())
    for t in range(1, T+1):
        print("Case #%d:" % t, solve())

