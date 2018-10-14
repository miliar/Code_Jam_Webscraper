#! /usr/bin/python
# -*-coding:Utf-8 -*

def readint():    return int(raw_input())
def readarray(f): return map(f, raw_input().split())

N, W, L = (0,0,0)

def fillRect(todo, P, x1, y1, x2, y2):
    global W,L
    for (i, r) in todo:
        left = -r if x1 == 0 else x1
        right = W+r if x2 == W else x2
        up = -r if y1 == 0 else y1
        down = L+r if y2 == L else y2
        if right-left >= 2*r and down-up >= 2*r:
            P[i] = (left + r, up + r)
            todo.remove((i,r))
            fillRect(todo, P, left+2*r, y1, x2, up+2*r)
            fillRect(todo, P, x1, up+2*r, x2, y2)
            return

T_ = readint()
for t_ in range(T_):
    print 'Case #'+str(t_+1)+':',
    
    N, W, L = readarray(int)
    R = list(enumerate(readarray(int)))
    R.sort(key=(lambda (i,j):-j))
    P = [(0,0)] * N
    fillRect(R, P, 0, 0, W, L)
    for (x,y) in P:
        print x,y,
    print
