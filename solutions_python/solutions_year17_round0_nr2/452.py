def tidy(s):
    if len(s) == 1:
        return s
    digs = [int(c) for c in s]
    n  = len(s)
    for i in xrange(1, n):
        if digs[i] < digs[i-1]:
            break
    while i > 0:
        if digs[i] < digs[i-1]:
            digs[i-1] -= 1
            i -= 1
        else:
            break
    tail = '9' * (n-i-1)
    if i > 0:
        return ''.join(map(str,digs[:i+1])) + tail
    else:
        if digs[i] == 0:
            return tail
        else:
            return str(digs[0]) + tail


if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        s = raw_input()
        print "Case #{}: {}".format(i, tidy(s))
