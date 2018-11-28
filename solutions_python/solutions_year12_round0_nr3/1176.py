uN = []
uM = []

def check(n,m):
    for i in range(len(uN)):
        if(n == uN[i] and m == uM[i]):
            return 0
    uN.append(n)
    uM.append(m)
    return 1

def findPairs(A,B,n):
    pairs = 0
    if(len(str(n))) == 1:
        return 0
    nS = str(n)
    for i in range(len(nS)):
        mS = nS[-i:-1] + nS[-1] + nS[0:-i]
        m = int(mS)
        if(A <= n and n < m and m <= B):
            #print("{0} <= {2} < {3} <= {1}".format(A,B,n,m))
            pairs += 1 * check(n,m)
    return pairs

f = open('b.in','r')
cases = int(f.readline())
for c in range(cases):
    uN = []
    uM = []
    limits = f.readline().rstrip().split(' ')
    A = int(limits[0])
    B = int(limits[1])
    pairs = 0
    for n in range(A,B+1):
        pairs = pairs + findPairs(A,B,n)
    print("Case #" + str(c+1) + ": " + str(pairs))