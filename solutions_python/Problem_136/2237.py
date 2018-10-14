def findTime(C,F,X):
    cps = 2
    t = 0
    while True:
        t1 = X/cps
        t2 = X/(cps + F)
        cTime = C/cps
        
        if t1 < cTime + t2:
            return t+t1
        t += cTime
        cps += F

f = open('B-large.in','r')
g = open('B-large.out','w')
a = f.read()
b = a.split('\n')

cases = (int)(b[0])

for i in range(0,cases):
    params = b[i+1].split(" ")
    C = (float)(params[0])
    F = (float)(params[1])
    X = (float)(params[2])

    g.write("Case #"+(str)(i+1)+": "+(str)(findTime(C,F,X))+"\n")

f.close()
g.close()
