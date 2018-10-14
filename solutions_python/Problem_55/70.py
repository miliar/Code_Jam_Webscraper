from itertools import cycle

def readint(): return int(raw_input())

def readints(): return [ int(x) for x in raw_input().split() ]

def calcincomes(glst, k):
    ret = []
    numr = 0
    already = []
    first = -1
    for i,x in cycle(enumerate(glst)):
        if numr + x <= k and first != i:
            numr += x
            if first == -1:
                first = i
        else:
            already.append(first)        
            ret.append(numr)
            numr = x
            first = i
            if i in already:
                loopstart = already.index(i)
                return ret[:loopstart],ret[loopstart:]

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        R,k,N = tuple(readints())
        glst = readints()
        head,loop = calcincomes(glst,k)

        headincome = sum(head)
        R -= len(head)

        loopincome = sum(loop) * int(R / len(loop))
        R -= int(R / len(loop)) * len(loop)

        tailincome = sum(loop[:R % len(loop)])

        income = headincome + loopincome + tailincome

        print "Case #%d: %d" % (i+1,income)
