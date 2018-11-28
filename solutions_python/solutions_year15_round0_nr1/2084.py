def gl(f, splitchar=' '):
    return map(f, raw_input().split(splitchar))

def g(f):
    return f(raw_input())

dummy=g(int)
for hur in xrange(dummy):
    t, v = gl(str)
    c = 0
    ans = 0
    for i, val in enumerate(v):
        if c < i:
            ans += i - c
            c += i - c
        c += int(val)
    
    print "Case #%d:" % (hur+1), ans
            
