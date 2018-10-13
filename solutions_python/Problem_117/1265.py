import sys
from multiprocessing import Pool

def findmax(data):
    res = list()
    for row in data:
        res.append(max(row))
    return res

def main(data):
    n,m,lawn = data
    rowmax = findmax(lawn)
    columnmax = findmax(zip(*lawn))
    for i in range(n):
        for j in range(m):
            h = lawn[i][j]
            if h < rowmax[i] and h < columnmax[j]:
                return "NO"
    return 'YES'
    

if __name__ == "__main__":
    test = False
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        test = True
        f = open("test.txt")
    T = int(f.readline())
    data = list()
    
    for i in range(T):
        N,M = map(int, f.readline().split())
        lawn = list()
        for j in range(N):
            lawn.append(map(int, f.readline().split()))
        data.append((N,M,lawn))
        
    pool = Pool()
    if test:
        result = map(main, data)
    else:
        result = pool.map(main, data)

    for i in range(T):
        print "Case #%d: %s" % (i+1, result[i])
        