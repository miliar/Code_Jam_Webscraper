def is_tidy(x):
    x = str(x)
    l = len(x)
    for i in xrange(l):
        if i and int(x[i]) < int(x[i-1]):
            return False
    return True

def untidy_index(x):
    x = str(x)
    l = len(x)
    for i in xrange(l):
        if i and int(x[i]) < int(x[i-1]):
            return i-1
    return -1

def prev_tidy(x):
    if is_tidy(x):
        return x
    x = str(x)
    l = len(x)
    while not is_tidy(x):
        if len(x) > l:
            break
        i = untidy_index(x)
        # print '- ', x
        if i < l-1:
            _x = ''
            for _ in xrange(l):
                if _ <= i:
                    _x += x[_]
                else:
                    _x += '9'
            x = _x
        if x[i] != '0':
            x = x[:i] + str(int(x[i])-1) + '9' + x[i+2:]
        else:
            x = x[:i] + '99' + x[i+2:]
        # print '-- ', x
    return str(int(x))

T = input()
for _ in xrange(T):
    N = input()
    ret = prev_tidy(N)
    print "Case #%s: %s" % (_+1, ret)