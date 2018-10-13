def fliper(s):
    b = ''
    for i in s:
        if i == '-':
            b +='+'
        else:
            b += '-'
    return b

def happysides(s, n):
    a, ls = 0, len(s)
    for i in xrange(ls-n+1):
        if s[i] == '-':
            s = s[0:i] + fliper(s[i:i+n]) + s[i+n:]
            a+=1
    if '-' in s:
        return None
    return a

t=int(raw_input())
for cas in xrange(1,t+1):
    s,fig=[str(s) for s in raw_input().split(" ")]
    n = int(fig)
    solu = happysides(s,n)
    if solu == None:
        print "Case #{}: {}".format(cas, 'IMPOSSIBLE')
    else:
        print "Case #{}: {}".format(cas, solu)
