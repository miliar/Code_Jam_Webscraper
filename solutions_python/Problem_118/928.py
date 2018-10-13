import math

pal_lst = []

def ary():
    return [int(e) for e in raw_input().split()]

def getcookie(n):
    ns = str(n)
    l = len(ns)
    hf = ns[:l/2]
    if l == 1:
        hf = ns
        mid = -2
    elif l%2:
        mid = int(ns[l/2])
    else:
        mid = -1
    return int(hf), mid
    
def getpal(cookie):
    a, b = cookie
    _a = str(a)
    if b == -2:
        r = _a
        a += 1
        if a == 10:
            a = 1
            b = -1
    elif b > -1:
        _b = str(b)
        b += 1
        if b == 10:
            b = 0
            a += 1
            if len(_a) <> len(str(a)):
                b = -1
        r = '%s%s%s'%(_a, _b, _a[::-1])
    else:
        _b = ''
        a += 1
        sa = str(a)
        if len(_a) <> len(sa):
            b = 0
            a = int(sa[:-1])
        r = '%s%s%s'%(_a, _b, _a[::-1])
    return int(r), (a, b)
    
def isPal(x):
    y = 0
    z = x
    while x:
        d = x%10
        y = y*10+d
        x /= 10
    if y == z:
        return True
    return False

def sqrt(aa, cond):
    a = math.sqrt(aa)
    if a - int(a) and cond:
        a = int(a) + 1
    else:   
        a = int(a)
    return a
    
def genpallst(aa, bb):
    a = sqrt(aa, True)
    b = sqrt(bb, False)
    ck = getcookie(a)

    while True:
        p, ck = getpal(ck)
        if p < a:
            continue
        if p > b:
            break
        if isPal(p*p):
            pal_lst.append(p*p)

def solve(t, A, B):
    rc = 0
    for p in pal_lst:
        if p >= A and p <= B:
            rc += 1
    print 'Case #%d: %s'%(t, rc)
    
def main():
    T = int(raw_input())
    genpallst(1, pow(10,14))
    for t in range(1, T+1):
        A, B = ary()
        solve(t, A, B)
    
main()