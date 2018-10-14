def translate(s, cas):
    """
    >>> translate('ejp mysljylc kd kxveddknmc re jsicpdrysi', 1)
    'Case #1: our language is impossible to understand'
    >>> translate('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 2)
    'Case #2: there are twenty six factorial possibilities'
    >>> translate('de kr kd eoya kw aej tysr re ujdr lkgc jv', 3)
    'Case #3: so it is okay if you want to just give up'
    """
    g = 'ynficwlbkuomxsevzpdrjgthaq'
    a = 'abcdefghijklmnopqrstuvwxyz'
    st = ''
    for c in s:
        if c in g:
            st += a[g.index(c)]
        else:
            st += c
    #XcWq
    return 'Case #%d: %s' % (cas, st)

if __name__ == '__main__':
    import sys
    f = sys.stdin
    T = int(f.readline())
    for tc in range(1, T + 1):
        s = f.readline().split('\n')[0]
        print translate(s, tc)
    #import doctest
    #doctest.testmod()
    
# Input
# 3
# ejp mysljylc kd kxveddknmc re jsicpdrysi
# rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
# de kr kd eoya kw aej tysr re ujdr lkgc jv


# Output
# Case #1: our language is impossible to understand
# Case #2: there are twenty six factorial possibilities
# Case #3: so it is okay if you want to just give up