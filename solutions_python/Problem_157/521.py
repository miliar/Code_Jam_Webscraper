lines = open("C-large.in").read().split("\n")
T = int(lines[0])

def mul(a,b):
    if a=='1':
        return 0,b
    elif b=='1':
        return 0,a
    elif a=='i':
        return {'i':(1,'1'),'j':(0,'k'),'k':(1,'j'),}[b]
    elif a=='j':
        return {'i':(1,'k'),'j':(1,'1'),'k':(0,'i'),}[b]
    else:
        return {'i':(0,'j'),'j':(1,'i'),'k':(1,'1'),}[b]

def mul1(a1,b1):
    
    neg =  (a1[0] == '-') ^ (b1[0] == '-')
    neg1, res = mul(a1[-1],b1[-1])
    return ('-' if (neg^neg1) else '') + res

def collapse(mult):
    if len(mult) == 1:
        return mult
    if len(mult) == 2:
        return mul1(mult[0],mult[1])
    else:
        p1 = mult[:len(mult)/2]
        p2 = mult[len(mult)/2:]
        return mul1(collapse(p1),collapse(p2))
def f(lx, st):
    lst,xst = lx.split(" ")
    L = int(lst)
    X = int(xst)
    
    need = ['i','j','k']
    used = 0
    curr = '1'
    for x in xrange(X):
        for ch in st:
            curr = mul1(curr,ch)
            used += 1
            if need and (curr == need[0]):
                curr = '1'
                used = 0
                need = need[1:]
            if used > 40000:
                return False
        if not need:
            collapsed = collapse(st)
            xleft = (X - x - 1) % 4
            for i in xrange(xleft):
                curr = mul1(curr, collapsed)
            return curr == '1'
    
    return False

for i in xrange(1,T+1):
    out = f(lines[2*i-1],lines[2*i])
    print "Case #%d: %s" % (i, "YES" if out else "NO")