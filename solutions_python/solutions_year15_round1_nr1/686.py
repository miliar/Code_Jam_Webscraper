#!/usr/bin/python

def metodo1(m):
    cont = 0
    ma = 0
    for mi in m:
        if mi < ma:
            cont += ma - mi
        ma = mi
    return cont

def maxDiff(m):
    ma = 0
    max = 0
    for mi in m:
        if max < (ma - mi):
            max = ma - mi
        ma = mi
    return max
def metodo2(m):
    vel = maxDiff(m)
    m_vel = vel
    ma = 0
    mush = 0
    for mi in m[:-1]:
        mush += mi if mi < m_vel else m_vel
    return mush

def graba(case, sol1, sol2):
    global fo
    fo.write("Case #" + str(case) + ": " + str(sol1) + " " + str(sol2) + "\n")

fi = open("A-large.in",'r')
fo = open("A-large.out",'w')
T = int(fi.readline())

for case in range(1,T+1):
    N = int(fi.readline())
    m = [int(x) for x in fi.readline().split()]
    sol1 = metodo1(m)
    sol2 = metodo2(m)
    graba(case, sol1, sol2)

fo.close()
fi.close()
