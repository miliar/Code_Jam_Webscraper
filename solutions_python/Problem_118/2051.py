

ans = []

def ok(ss):
    m = int(ss)**2
    return str(m) == str(m)[::-1]

def sq(s):
    m = int(s)
    return str(m*m)

def pos(s):
    n = len(s)
    under = str( int(s)**2 + (10**(n+1)) )[-n:]
    inv_under = int( under[::-1] )
    m = int(s[::-1])
    return m*m < (inv_under+1) * (10**(n-1)) and (m+1)*(m+1)>= (inv_under+1) * (10**(n-1))



def next(s):
    if len(s)>=9:return
    if ok(s[::-1] + s):
        ans.append(sq (s[::-1]+s))
    for v in xrange(10):
        s2 = s[::-1] + str(v) + s
        if ok(s2):
            ans.append(sq(s2))
        s3 = str(v) + s
        if pos(s3):
            next(s3)

def test():
    for m in xrange(1,10000):
        for v in [int( str(m) + str(m)[::-1] ), int( str(m) + str(m)[-2::-1] )]:
            #if m<=100:print m,v
            s = str(v*v)
            if s==s[::-1]:
                if s not in ans:
                    print "NO", s
        

def main():
    for v in xrange(1,4):
        next(str(v))
    
    ans.append('1')
    ans.append('4')
    ans.append('9')
    test()
    h = map(int, ans)
    T = int(raw_input())
    for t in xrange(T):
        cnt = 0
        a,b = map(int, raw_input().split())
        for v in h:
            if a<=v<=b:cnt+=1
        print "Case #%s: %s"%(t+1,cnt)



main()