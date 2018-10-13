import sys
from multiprocessing import Pool

def main(data):
    n,k,b,t,X,V = data
    s = 0
    ret = 0
    if k == 0:
        return str(0)
    p = k
    for i in range(n-1, -1, -1):
        d = X[i] + V[i] * t 
        if d >= b:
            p -= 1
            ret += s
            if p == 0:
                return str(ret)
        else:
            s += 1
    else:
        return "IMPOSSIBLE"

if __name__ == "__main__":
    f = open(sys.argv[1])
#    f = open("c.txt")
    T = int(f.readline())
    data = []
    for i in range(T):
        n,k,b,t = map(int, f.readline().split())
        x = map(int, f.readline().split())
        v = map(int, f.readline().split())
        data.append((n,k,b,t,x,v))
    
    pool = Pool()
    r = pool.map(main, data)
#    r = map(main, data)
    for i in range(T):
        print "Case #%d: %s" % (i+1, r[i]) 