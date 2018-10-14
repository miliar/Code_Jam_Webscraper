import sys
import math
import time
from Queue import Queue
from sets import Set

class pythonin:
    _data = []
    _ldata = []
    _cur = 0
    _lcur = 0
    
    def __init__(self):
        while True:
            try: self._ldata.append(raw_input())
            except EOFError : break

    def _convert(self):
        if self._lcur == len(self._ldata) : return
        l = self._ldata[self._lcur].split(" ")
        self._lcur += 1
        for x in l :
            if x != "" and x != "\t" :
                self._data.append(x)
        
    def eof(self) : 
        self._convert()
        return self._cur == len(self._data)

    def nextToken(self) :
        if self.eof() : return
        self._cur += 1
        return self._data[self._cur - 1]
    
    def nextInt(self) :
        return int(self.nextToken())
    
    def nextFloat(self) :
        return float(self.nextToken())
    
    def nextLine(self) :
        if self._lcur == len(self._ldata) : return 
        self._lcur += 1
        return self._ldata[self._lcur - 1]
    
sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")

pin = pythonin()

cacheFact = [1]

def fact(n) :
    if n < len(cacheFact) : return cacheFact[n]
    x = cacheFact[len(cacheFact) - 1]
    for i in xrange(len(cacheFact), n + 1) :
        x *= i
        cacheFact.append(x)
    return float(cacheFact[n])

def cnk(n, k) : 
    return fact(n) / fact(n - k) / fact(k)

cacheF = [1]

def f(n) :
    if n < len(cacheF) : return cacheF[n]
    res = f(n - 1) * n 
    if n % 2 == 0 : res += 1
    else          : res -= 1
    cacheF.append(res)
    return float(res)

def g(n, k) :
    w = cnk(n, k)
    u = f(k)
    return float(cnk(n, k) * f(k))

def pg(n, k) :
    return (float)(g(n, n - k)) / fact(n)

cacheDP = [0, 0]

def dp(n) : 
    if n < len(cacheDP) : return cacheDP[n]
    q = 1.0 - pg(n, 0)
    res = 1.0 - q
    for i in xrange(1, n + 1) :
        r = pg(n, i)
        z = dp(n - i) + 1
        res += z * r
    
    res /= float(q)
    
    cacheDP.append(res)
    return res


TC = pin.nextInt()

for tc in xrange(1, TC + 1) :
    n = pin.nextInt()
    a = [pin.nextInt() - 1 for i in xrange(0, n)]
    s = []
    used = [False for i in xrange(0, n)]
    for i in xrange(0, n):
        if not used[i] :
            sz = 0
            cur = i
            while True :
                sz += 1
                used[cur] = True
                cur = a[cur]
                if cur == i : break
            s.append(sz)  
    res = 0
    for x in s :
        res += dp(x)    

    print "Case #" + str(tc) + ":", res
    

#print ("Press any key to continue")
#raw_input() 
