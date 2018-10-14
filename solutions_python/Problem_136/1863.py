'''
Created on 12/04/2014

@author: tianyizhu
'''
from multiprocessing import Process, Manager
from __builtin__ import xrange

def check(c, f, x, n):
    ans = 0.0
    for i in xrange(n):
        ans += c / (i * f + 2.0)
    ans += x / (n * f + 2.0)
    return ans

def db(start, c, f, x, a, res, ci):
    aa = 1
    flag = False
    while aa > 0:
        cc = start + aa * a
        if cc < 0:
            aa /= 2
            continue
        ans = check(c, f, x, cc)
        if ans < res[ci]:
            flag = True
            res[ci] = ans
            aa *= 2
            start = cc
        else:
            aa /= 2
    if flag:
        db(start, c, f, x, -a, res, ci)
        
        

def ff(ci, res, c, f, x):
    res[ci] = x / 2.0
    db(0, c, f, x, 1, res, ci)
    
if __name__ == "__main__":
    ps = []
    manager = Manager()
    fin = open("cca.in", "r")
    fout = open("cca.out", "w")
    t = int (fin.readline())
    res = manager.list(range(t))
    for ci in xrange(t):
        numbers = fin.readline().split(" ")
        c = float(numbers[0])
        f = float(numbers[1])
        x = float(numbers[2]) 
        p = Process(target=ff, args=(ci, res, c, f, x))
        ps.append(p)
        p.start()
    for ci in xrange(t):
        ps[ci].join()
        fout.write("Case #%d: %s\n" % (ci + 1, str(res[ci])))
    fout.close()
    fin.close()
