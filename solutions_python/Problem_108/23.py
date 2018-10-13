#! /usr/bin/python
# -*-coding:Utf-8 -*

def readint():    return int(raw_input())
def readarray(f): return map(f, raw_input().split())

T_ = readint()
for t_ in range(T_):
    print 'Case #'+str(t_+1)+':',

    N = readint()
    V = []
    for i in range(N):
        d,l = readarray(int)
        V.append((d,l))
    V.append((readint(),0)) 
    B = [V[0][0]]
    for i in range(1,N+1):
        b = -1
        for j in range(i-1, -1, -1):
            if B[j] >= V[i][0] - V[j][0]:
                b = max(b, min(V[i][0] - V[j][0], V[i][1]))
        B.append(b)
    if B[-1] > -1:
        print "YES"
    else:
        print "NO"


