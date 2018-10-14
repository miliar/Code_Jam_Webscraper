#!/usr/bin/python3

def findFirst(l):
    for j in range(len(l) - 1):
        if l[j] > l[j+1]:
            return j
    return -1

def solve(s):
    l = list(s)
    while True:
        j = findFirst(l)
        if j == -1:
            return ''.join(l if l[0] != '0' else l[1:])
        l[j] = str(int(l[j]) - 1)
        for k in range(j+1, len(l)):
            l[k] = '9'

n = int(input())
for t in range(n):
    s = input()
    print('Case #{}: {}'.format(t+1, solve(s)))
