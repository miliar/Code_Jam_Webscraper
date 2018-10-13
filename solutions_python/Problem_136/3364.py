def step(c,f,x,s):
    if x / s < (x / (s+f)) + (c/s) :
        return x / s
    else:
        return c/s + step(c,f,x,s+f)
import sys
sys.setrecursionlimit(10000)
r = open('data2.txt')
w = open('out.txt','w')
for case in range(int(r.readline())):
    c,f,x = r.readline().strip().split()
    c,f,x = float(c),float(f),float(x)
    print(case)
    w.write('Case #'+str(case+1)+': '+ str('{0:.7f}'.format(step(c,f,x,2.0)))+'\n')
w.close()
