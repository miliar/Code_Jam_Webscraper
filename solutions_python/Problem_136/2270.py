import sys

a = open("input.in")
b = open("output.txt","w")

def game(c,F,x):
    f = 2
    time = 0
    t1 = x/f
    cookie = 0
    if (x < c):
        return "%.7f"%(x/2)
    while True:
        t3 = c/f
        f += F
        if t3+x/f <= t1:
            time += t3
            #print c/f
            t1 = x/f
        else:
            time += t1
            break
    return "%.7f"%time


for i in xrange(int(a.readline())):
    c,F,x = map(float,a.readline().split())
    line = "Case #%d: %s\n"%(i+1,game(c,F,x))
    print line
    b.write(line)
        
        
    
