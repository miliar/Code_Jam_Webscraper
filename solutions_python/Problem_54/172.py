from multiprocessing import Process, Queue, Pool
from Queue import Empty
import sys

def gcd(a, b):
    while b:
        r = a % b
        a = b
        b = r
    return a

def abs(a):
    if a < 0:
        return -a
    return a

def getT1(data):
    if len(data) == 2:
        a = max(data[0], data[1])
        b = min(data[0], data[1])
        if a % b == 0:
            return b
        if a - b < b:
            return a - b
        y = a - 2 * b
#        g = gcd(a, b)
#        p = a / g
#        q = b / g
#        n = 0
#        for x in range(1, q):
#            if (p+x) % (q+x) == 0:
#                n = (p+x) / (q+x)
#        y = (a - n * b) / (n - 1)
        return b + y
    data.sort()
    nset = set()
    for i in range(1, len(data)):
        nset.add(data[i] - data[i-1])
    d = sorted(nset)
    if d[0] == 0:
        d.pop(0)
    while len(nset) > 1:
        sd = d[0]
        if sd == 1:
            return 1
        nset = set()
        for t in d:
            nset.add(gcd(t, sd))
        d = sorted(nset)
    return nset.pop()

def gcdN(data):
    n = len(data)
    d = data[n-1]
    j = n - 2
    while d != 1 and j >= 0:
        d = gcd(data[j], d)
        j -= 1
    return d

def getT(data):
    data = sorted(set(data))
    l = len(data)
    if l == 1:
        return data[0]
    elif l == 2:
        return data[1] - data[0]
    else:
        nset = set()
        for i in range(l):
            p = data[i]
            for j in range(i+1, l):
                nset.add(data[j] - p)
        d = sorted(nset)
        if len(d) < 2:
            return d[0]
        return gcdN(d)
        
        
    
def getY(line):
    data = [int(i) for i in line.split()]
    data.pop(0)
    
    T = getT(data)
    r = data[0] % T
    if r == 0:
        return 0
    else:
        return T - (data[0] % T)

def main(inqueue, outqueue):
    while True:
        line = None
        try:
            index, line = inqueue.get(False)
        except Empty:
            return
        y = getY(line)
        outqueue.put((index, y))
        inqueue.task_done()

if __name__ == "__main__":
    f = open(sys.argv[1])
    lines = f.readlines()
    C = int(lines[0])
    lines = lines[1:C+1]
#    inqueue = Queue()
#    outqueue = Queue()
#    
#    for i in range(C):
#        inqueue.put((i, lines[i]))
#    for i in range(4):
#        p = Process(target=main, args=(inqueue, outqueue))
#        p.start()
#        
#    result = [0] * C
#    inqueue.join()
#    while not outqueue.empty():
#        i, y = outqueue.get()
#        result[i] = y
#    pool = Pool()
#    result = pool.map(getY, lines)
    result = map(getY, lines)
    for i in range(0, C):
        print "Case #%d: %d" % (i+1, result[i])





                