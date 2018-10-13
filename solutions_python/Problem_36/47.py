import sys
sys.setrecursionlimit(20000)
inp = open("d:\\incoming\\c-large.in", "r")
#inp = open("d:\\incoming\\c-small-attempt0.in", "r")
#inp = open(".\\c.in", "r")
outp = open(".\\c.out", "w")

global cache, a, b

def go(ai, bi):
    if bi == len(b): return 1
    if ai == len(a): return 0
    if (ai,bi) in cache: return cache[(ai,bi)]
    ret = go(ai+1, bi) % 10000
    if a[ai] == b[bi]:
        ret = (ret + go(ai + 1, bi + 1)) % 10000
    cache[(ai,bi)] = ret
    return ret

cases = int(inp.readline())
b = "welcome to code jam"
for cc in xrange(cases):
    a = inp.readline().rstrip("\n\r")
    cache = {}
    res = "Case #%d: %.4d" % (cc+1, go(0, 0))
    print res
    outp.write(res + "\n")
outp.close()
