import sys

def go(upto, engine):
    global cache, seq, s
    if upto == len(seq): return 0
    if seq[upto] == engine: return 2**32
    if cache[upto][engine] != -1: return cache[upto][engine]
    ret = 2**32
    for nextengine in range(s):
        cand = go(upto+1, nextengine)
        if nextengine != engine:
            cand += 1
        ret = min(ret, cand)
    cache[upto][engine] = ret
    return ret

def pro(inp = sys.stdin, outp = sys.stdout):
    global cache, seq, s
    cases = int(inp.readline())
    for cc in range(cases):
        s = int(inp.readline())
        engines = {}
        for j in range(s):
            e = inp.readline().rstrip("\n")                                      
            engines[e] = j
        q = int(inp.readline())
        seq = []
        for j in range(q):
            e = inp.readline().rstrip("\n")
            seq.append(engines[e])
        cache = [[-1] * (s+10) for i in range(q+10)]
        ret = q+1
        for i in range(q,0,-1):
            for j in range(s):
                go(i, j)
        for j in range(s): ret = min(ret, go(0, j))
        outp.write("Case #%d: %d\n" % (cc+1, ret))
        
def r(infile, outfile):
    a = open(infile, "r")
    b = open(outfile, "w")
    pro(a, b)
    a.close()
    b.close()
