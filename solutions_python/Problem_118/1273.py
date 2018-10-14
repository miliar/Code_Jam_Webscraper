#!python
import sys

def readint(): return int(raw_input())
def readints(): return [ int(x) for x in raw_input().split() ]
def readline(): return raw_input()
def skipline(): return raw_input()

def ispn(num):
    s = str(num)
    l = (len(s)+1)/2
    return s[:l] == s[-l::][::-1]

def lxrange(c,e):
    while c < e:
        c += 1
        yield c


def genpn(s,e):
    for x in lxrange(0,e):
        s = str(x)
        rs = s[::-1]
        pn1 = int(s+rs[1:])
        pn2 = int(s+rs)
        if pn2 <= e:
            yield pn2
            if pn1 != pn2:
                yield pn1
        elif pn1 <= e:
            yield pn1
        else:
            return


def genfsn(s,e):
    for x in genpn(1,e):
        sn = x ** 2
        if ispn(sn) and s <= sn <= e:
            #print "%d * %d == %d" % (x,x,x**2)
            yield 1

def solve(s,e):
    return "%d" % sum(genfsn(s,e))

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        s, e = tuple(readints())
        
        print "Case #%d: %s" % ( i+1, str(solve(s,e)))
