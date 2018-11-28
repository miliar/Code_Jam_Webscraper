import sys

input = {"ejp mysljylc kd kxveddknmc re jsicpdrysi": "our language is impossible to understand", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd": "there are twenty six factorial possibilities", "de kr kd eoya kw aej tysr re ujdr lkgc jv": "so it is okay if you want to just give up"}

def generate(inMap):
    outMap = {}
    for k in inMap:
        v = inMap[k]
        for i in xrange(len(k)):
            outMap.setdefault(k[i], v[i])
    outMap.setdefault('q', 'z')
    outMap.setdefault('y', 'a')
    outMap.setdefault('e', 'o')
    outMap.setdefault('z', 'q')
    return outMap

def inverse(inMap):
    outMap = {}
    for k in inMap:
        v = inMap[k]
        outMap.setdefault(v, k)
    return outMap

def translate(map, s):
    o = ""
    for c in s:
        o += map[c]
    return o

def solve(f = None):
    map = generate(input)
    answers = []
    if f != None:
        handle = open(f)
    else:
        handle = sys.stdin
    n = int(handle.readline())
    for i in xrange(n):
        s = handle.readline().strip()
        answers.append(translate(map, s))
    for i in xrange(n):
        print "Case #%d: %s" % (i+1, answers[i])

    
