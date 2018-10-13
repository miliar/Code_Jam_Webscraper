def gl(f, splitchar=' '):
    return map(f, raw_input().split(splitchar))

def g(f):
    return f(raw_input())

t=g(int)
for i in xrange(t):
    first=g(int) - 1
    cards1=[gl(int) for _ in xrange(4)]
    second=g(int) - 1
    cards2=[gl(int) for _ in xrange(4)]
    ans = set(cards1[first]) & set(cards2[second])
    print "Case #%d:" % (i + 1),
    if len(ans) == 1:
        print list(ans)[0]
    elif len(ans) == 0:
        print "Volunteer cheated!"
    else:
        print "Bad magician!"
    
