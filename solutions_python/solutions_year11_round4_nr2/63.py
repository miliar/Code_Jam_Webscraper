#!/usr/bin/python

def inb(i,j,x,y,k):
    if (i == x) + (i == x + k - 1) + (j == y) + (j == y + k - 1) >= 2:
        return False
    return (x <= i <= x + k -1 and y <= j <= y + k - 1)

def tryone(x,y,k):
    if x + k - 1 >= r or y + k - 1>= c:
        return False
    cx = 0.0
    cy = 0.0
    mass = 0
    co = 0
    for i in range(r):
        for j in range(c):
            if not inb(i,j,x,y,k):
                continue
            co +=1
            rm = (m[i][j] + d)
            mass += rm
            cx += i *rm
            cy += j *rm
    if mass == 0:
        return False
    cx/=mass
    cy/=mass
    return (cx == x + (k - 1.0)/2.0 and cy == y + (k - 1.0)/2.0) 


def tryall(k):
    for i in range(r):
        for j in range(c):
            if tryone(i,j,k):
                return True  

def solve():
    best = 0
    for k in range(3,min(c,r)+1):
        if tryall(k):
            best = k
    if best == 0:
        return 'IMPOSSIBLE'
    return best

r = input()
for case in range(1,r+1):
    l = map(int,raw_input().split())
    r,c,d = tuple(l)
    d = float(d)
    m = []
    for _ in range(r):
        m.append(map(int,list(raw_input())))
    print "Case #%s: %s" % (case, solve())
