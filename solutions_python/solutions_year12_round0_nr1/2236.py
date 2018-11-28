

def solve(data, was):
    out = []

    for i in xrange(len(data)):
        out.append(was[data[i]])



    return ''.join(out)



if __name__ == '__main__':

    str = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
    tmp = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"

    was = {'q' : 'z', 'z': 'q'}
    for i in xrange(len(str)):
        if not was.has_key(tmp[i]):
            was[tmp[i]] = str[i]

    t   = {}
    for i in was:
        t[was[i]]   = i

    import sys
    T   = int(sys.stdin.readline())
    for i in xrange(T):
        data    = sys.stdin.readline().strip()
        out = solve(data, t)
        print "Case #%s: %s" % (i+1, out)
