#!/bin/python
#import sys
#sys.stdin = file("sample.in")

def readint(): return int(raw_input())

def readints(): return [ int(x) for x in raw_input().split() ]

def orop(cs):
    ret = 0
    for c in cs:
        ret = ret ^ c
    return ret

m = {
}

wm = {
"kd":"is",
"ejp":"our",
"ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv": "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up",
"qz":"zq"
}

def makemap():
    global m, wm
    for k,v in wm.items():
        for s,d in zip(k,v):
            if s in m.keys():
                if m[s] != d:
                    raise Exception("conflict %s->%s, old:%s, new:%s" % (k,v,s,d))
            m[s] = d
            if len(set(m.values())) != len(m.values()):
                raise Exception("conflict %s->%s, value:%s" % (k,v,d))

makemap()

#print "".join([chr(ord('a')+i) for i in range(0,26) if chr(ord('a')+i) not in m.keys()])
#print "".join([chr(ord('a')+i) for i in range(0,26) if chr(ord('a')+i) not in m.values()])

def onemap(c):
    try:
        return m[c]
    except:
        return c

def solve(txt):
    return "".join(onemap(c) for c in txt)

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        text = raw_input()
        print "Case #%d: %s" % ( i+1, str(solve(text)))
