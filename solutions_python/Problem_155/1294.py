#!/usr/bin/python

def solve(smax, aud):
    suma = 0
    sol = 0
    for k in range(len(aud)):
        c = int(aud[k])
        if c == 0:
            continue
        if (suma + sol) >= k:
            pass
        else:
            sol = k - suma
        suma += c
    return sol
def graba(case, sol):
    global fo
    fo.write("Case #" + str(case) + ": " + str(sol) + "\n")
fi = open("A-large.in",'r')
fo = open("A-large.out",'w')
T = int(fi.readline())

for case in range(1,T+1):
    line = fi.readline().split()
    smax, audience = int(line[0]), line[1]
    sol = solve(smax, audience)
    graba(case, sol)

fo.close()
fi.close
