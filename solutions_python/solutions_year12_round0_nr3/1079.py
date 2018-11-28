import fileinput

infile = fileinput.input()

def r(fn='none', splt=True):
    '''r(fn=none, splt=True)
    Example: N, = r(long)
    S = r(str,splt=False)
    '''
    inp = infile.readline()
    if splt:
        inp = inp.split()
        return map(fn, inp)
    else:
        return fn(inp)

recyc = []

def f(n, A, B):
    global recyc
    total = 0
    s = str(n)
    for x in range(1,len(s)):
        if s[x] >= s[0]:
            m = s[x:] + s[:x]
            if A <= n < int(m) <= B:
                if (n,int(m)) not in recyc:
                    recyc.append((n,int(m)))
                    total += 1
                #print n,m
    return total

T, = r(long)

for t in range(T):
    recyc = []
    D = r(int)
    A = D.pop(0)
    B = D.pop(0)
    ans = 0

    for n in range(A,B+1):
        ans += f(n, A, B)
    print "Case #%d: %d"%(t+1, ans)
