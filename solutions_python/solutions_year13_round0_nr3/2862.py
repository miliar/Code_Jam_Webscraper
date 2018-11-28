import math

def pal(x):
    for i in range(len(x)/2):
        if (x[i] != x[len(x)-1-i]):
            return False
    else:
        return True
    
def sqr(x):
    t = math.sqrt(x)
    if ((t - int(t)) != 0):
        return -13
    else:
        return int(t)

    
def fs (x):
    return (pal(x) and pal(str(sqr(int(x)))))

def fsInInterval(a,b):
    cnt = 0
    for i in range(a,b+1):
        if (fs(str(i))):
            cnt += 1
    else:
        return cnt

lines = [line.strip() for line in open('input.in')]
n = int(lines[0])

for i in range(1,n+1):
    print "Case #"+str(i)+": "+str(fsInInterval(int(lines[i].split()[0]),int(lines[i].split()[1])))

    
