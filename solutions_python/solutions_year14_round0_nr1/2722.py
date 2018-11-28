T = input()
for cas in xrange(T):
    x = input()
    a = [map(int, raw_input().split()) for _ in xrange(4)]
    y = input()
    b = [map(int, raw_input().split()) for _ in xrange(4)]
    res = set(a[x-1]) & set(b[y-1])
    s =  'Case #{0}: '.format(cas+1)
    if len(res)==0:
        print s + 'Volunteer cheated!'
    elif len(res)==1:
        print s + str(res.pop())
    else:
        print s + 'Bad magician!'
