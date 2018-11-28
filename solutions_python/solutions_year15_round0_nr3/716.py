import sys
inp = sys.stdin.readline
def get(a,b):
    d = {'1':{'1':'1','i':'i','j':'j','k':'k'} ,
            'i':{'1':'i','i':'-1','j':'k','k':'-j'}, 
            'j':{'1':'j','i':'-k','j':'-1','k':'i'}, 
            'k':{'1':'k','i':'j','j':'-i','k':'-1'}}
    return d[a][b]

def solve(L,X,S):
    S = S*X
    l = L*X
    sres = '1'
    eres = '1'
    iInd,kInd = 0,l-1
    iind,kind = iInd,kInd
    ssign = 1
    esign = 1
    while True:
        # print iInd,kInd
        for i in xrange(iInd,kind):
            sres = get(sres,S[i])
            if sres[0] == '-':
                ssign *= -1
                sres = sres[1]
            if sres == 'i':
                iind = i
                break
        # print sres
        if sres != 'i':
            return 'NO'
        for i in xrange(kInd,iind,-1):
            # print S[i],eres
            eres = get(S[i],eres)
            if eres[0] == '-':
                esign *= -1
                eres = eres[1]
            if eres == 'k':
                kind = i
                break
        # print eres
        if eres != 'k':
            return 'NO'
        iInd,kInd = iind,kind
        if kInd - iInd > 1:
            mres = '1'
            msign = 1
            for i in xrange(iInd+1,kInd):
                # print mres,S[i],i
                mres = get(mres,S[i])
                if mres[0] == '-':
                    msign *= -1
                    mres = mres[1]
            # print sres,mres,eres
            if mres == 'j' and ssign*esign*msign == 1 and sres == 'i' and eres == 'k':
                return 'YES'
        else:
            return 'NO'
        iInd += 1
        kInd -= 1
        # print sres,mres,eres
        # print iInd,kInd

for i in xrange(1, int(inp().strip())+1):
    L, X = map(int,inp().strip().split())
    S = inp().strip()
    print "Case #%d: %s" %(i,solve(L,X,S))