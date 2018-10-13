def readint():
    return int(raw_input())
def readfloat():
    return float(raw_input())
def readarray(N, foo=raw_input):
    return [foo() for i in xrange(N)]
def readlinearray(foo=int):
    return map(foo, raw_input().split())


case_number = readint()
for case in xrange(case_number):
    k = readint()
    s = None
    for i in range(4):
        t = readlinearray()
        if i == k - 1:
            s = set(t)
    k = readint()
    for i in range(4):
        t = readlinearray()
        if i == k - 1:
            s.intersection_update(t)
    if len(s) == 1:
        answer = str(list(s)[0])
    elif len(s) > 1:
        answer = 'Bad magician!'
    else:
        answer = 'Volunteer cheated!'
    print "Case #%s: %s" % (case + 1, answer)
