#!/usr/bin/python

from math import *

def breakNum(v):
    
    lst = []
    while (v):
        lst.append(v%10)
        v//=10
    return lst[::-1]

def isPalindrome(v):
    l = len(v)
    for i in range(l//2):
        if v[i]!=v[-i-1]:
            return False
    return True

def inc(v, carry=True, rev=False):
    solved = False
    if rev:
        ran = range(0, len(v))
    else:
        ran = range(len(v)-1, -1, -1)
    for i in ran:
        v[i] += 1
        if (v[i] != 10):
            solved = True
            break
        else:
            v[i] = 0
    if (not solved and carry):
        v.insert(0, 1)
    return v
    
def isqrt(n):
    x = n
    y = (x + n // x) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def countByDigits(d):
    numL = [0]*d
    for i in range(d):
        v[i] += 1
        v[-i-1] += 1
        if (v[i] == 10):
            v[i] = v[-i-1] = 0

def sqPerf(n):
    sq = isqrt(n)
    if sq*sq == n:
        return sq
    else:
        return False
      
def pal(sz, bein=[1,4]):
    if sz == 0:
        yield []
    elif sz == 1:
        for i in range(0, 10):
            yield [i]
    else:
        lst = [0]*(sz//2)
        lstn = [0]*(sz//2)
        if sz>=2:
            lst[0] = lstn[-1] = 1
        odd = sz%2 != 0
        while lst[0]!=0:          
            if lst[0] in bein:
                #sd = sum(lst)   
                if odd:
                    for i in xrange(0, 10):
                        if True:# sqPerf(sd+sd+i):
                            yield lst+[i]+lstn
                else:
                    if True:#sqPerf(sd+sd):
                        yield lst+lstn
            inc(lst, False)
            inc(lstn, False, True)
  
def lToN(l):
    n=0
    for i in l:
        n*=10
        n+=i
    return n

def findPalPerf2(digits):
    palPerf = []
    for v in range(1, digits//2+1):
        print "v ", v
        for pl in pal(v, [1,2]):
            n = lToN(pl)
            if not n: continue
            sq = n*n
            if isPalindrome(breakNum(sq)):
                #print sq, "sqrt: ", n
                palPerf.append(sq)

    return palPerf
    
#l = findPalPerf2(20)
#print l, len(l) 


def findPalPerf(digits):
    palPerf = []
    for v in range(1, digits):
        print "v ", v
        for pl in pal(v):
            n = lToN(pl)
            if not n: continue
            sq = sqPerf(n)
            if sq and isPalindrome(breakNum(sq)):
                s = sum(pl)
                sqd = sqPerf(s)
                print pl, n, sq, s, sqd
                palPerf.append(n)

    return palPerf
    
#l = findPalPerf(15)
#print l, len(l) 

def countPalSq(a, b):
    tot = 0
    numI = a
    numL = breakNum(a)
    while numI!=b+1:
        if (isPalindrome(numL)):
            sq = isqrt(numI)
            if sq*sq == numI:
                if (isPalindrome(breakNum(sq))):
                    print numI
                    tot += 1
        numI += 1
        inc(numL)
    return tot

#countPalSq(1, 100000000000000)

prePal = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001, 100220141022001, 102012040210201, 102234363432201, 121000242000121, 121242363242121, 123212464212321, 123456787654321, 400000080000004, 10000000200000001, 10002000300020001, 10004000600040001, 10020210401202001, 10022212521222001, 10024214841242001, 10201020402010201, 10203040504030201, 10205060806050201, 10221432623412201, 10223454745432201, 12100002420000121, 12102202520220121, 12104402820440121, 12122232623222121, 12124434743442121, 12321024642012321, 12323244744232321, 12343456865434321, 12345678987654321, 40000000800000004, 40004000900040004, 1000000002000000001, 1000220014100220001, 1002003004003002001, 1002223236323222001, 1020100204020010201, 1020322416142230201, 1022123226223212201, 1022345658565432201, 1210000024200000121, 1210242036302420121, 1212203226223022121, 1212445458545442121, 1232100246420012321, 1232344458544432321, 1234323468643234321, 4000000008000000004]

def countPalInRange(a, b):
    return reduce(lambda total, p: total+ (1 if p>=a and p<=b else 0), prePal, 0)

T = int(raw_input())
for i in range(1, T+1):
    a, b = map(int, raw_input().split(" ", 2))
    print "Case #%d: %d"%(i, countPalInRange(a, b))
			
