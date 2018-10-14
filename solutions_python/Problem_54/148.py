def readint(): return int(raw_input())

def readints(): return [ int(x) for x in raw_input().split() ]

def gdc(x,y):
    while y:
        x, y = y, x % y
    return x

def gdcs(lst):
    return reduce(gdc,lst)

def calcterms(lst):
    lst.sort()
    lst.reverse()
    ret = []
    prev = lst[0]
    for x in lst[1:]:
        ret.append(prev-x)
        prev = x
    return ret

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        lst = readints()
        ans = -lst[1] % gdcs(calcterms(lst[1:]))
        print "Case #%d: %d" % (i+1,ans)
        
