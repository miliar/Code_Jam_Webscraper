import sys
sys.setrecursionlimit(15000000)

def calc(s,c,f,x,r):
    while (x/r > c/r + x/(f+r)) :
        s += c/r
        r += f
    return s + x/r

f = open('B-large.in','r')
n = int(f.readline())
cases = []
for i in range(n):
    x = f.readline().split()
    y = calc(0.0,float(x[0]),float(x[1]),float(x[2]),2.0)
    cases.append('Case #'+`i+1`+': '+`y`)
f.close()
g = open('outputB.txt','w')
for z in cases :
    g.write(z+'\n')
g.close()