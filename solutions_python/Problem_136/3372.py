from itertools import count

def simulate(c,f,x,n):
    s = 2.0
    t = 0.0
    for i in range(n):
        t += c/s
        s += f
    return t + x/s

def result(input):
    (c,f,x) = map(float,input[0].split())
    t1 = simulate(c,f,x,0)
    for i in count(1):
        t2 = simulate(c,f,x,i)
        if t2 > t1: return t1
        else: t1 = t2
                        
f = open('B-small-attempt0.in')
r = f.readlines()
w = open('B-small-attempt0.out','w')

for i in range(int(r[0])):
    w.write('Case #%s: %s\n' % (str(i+1), result(map(lambda x:x.strip(),r[i+1:i+2]))))
f.close()
w.close()
