import sys
from multiprocessing import Pool

def main(data):
    n,m,N,M = data
    s = 0
    root = dict()
    for i in N:
        pwd = root
        entities = filter(None, i.split("/"))
        for e in entities:
            if e in pwd:
                pwd = pwd[e]
            else:
                pwd[e] = dict()
                pwd = pwd[e]
    for i in M:
        pwd = root
        entities = filter(None, i.split("/"))
        for e in entities:
            if e in pwd:
                pwd = pwd[e]
            else:
                pwd[e] = dict()
                pwd = pwd[e]
                s += 1
    return s
                

if __name__ == "__main__":
    f = open(sys.argv[1])
#    f = open("f.txt")
    T = int(f.readline())
    data = []
    for i in range(T):
        n,m = map(int, f.readline().split())
        N = []
        M = []
        for j in range(n):
            N.append(f.readline().strip())
        for j in range(m):
            M.append(f.readline().strip())
        data.append((n,m,N,M))
    
    pool = Pool()
    r = pool.map(main, data)
    for i in range(T):
        print "Case #%d: %d" % (i+1, r[i]) 