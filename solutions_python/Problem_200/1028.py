#!/usr/bin/python

def dec(c):
    return chr(ord(c) - 1)

def go(x):
    if x in ['', '0']: return ''

    rev = lambda p: len(x) - p - 1

    for i in xrange(len(x) - 1):
        if x[rev(i + 1)] > x[rev(i)]:
            y = x[:rev(i + 1)] if rev(i + 1) > 0 else ''
            y += dec(x[rev(i + 1)]) 
            return go(y) + '9' * (i + 1)

    return x

def main():
    N = int(raw_input())
    import pdb
    #pdb.set_trace()
    for i in xrange(N):
        print "Case #%d: %s" % (
            i + 1,
            (go(raw_input()) or '0')
        )

if __name__== "__main__":
    main()
