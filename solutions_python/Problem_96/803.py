import math

def count_dancers_at(cas, ngooglers, nsurprising, p, scores):
    """
    >>> count_dancers_at(1, 3, 1, 5, [15, 13, 11])
    'Case #1: 3'
    >>> count_dancers_at(2, 3, 0, 8, [23, 22, 21])
    'Case #2: 2'
    >>> count_dancers_at(3, 2, 1, 1, [8, 0])
    'Case #3: 1'
    >>> count_dancers_at(4, 6, 2, 8, [29, 20, 8, 18, 18, 21])
    'Case #4: 3'
    """
    njudges_r = (3 * 1.0)
    n = 0
    for g in scores:
        v = g / njudges_r
        v_ceil = int(math.ceil(v))
        #m_triplet = [v_ceil - 1, v_ceil, v_ceil]
        if v_ceil >= p:
            # if v - int(math.floor(v)) >= 0.6:
                # print 'v: ', v, ' v_ceil: ', int(math.floor(v)), ' p: ', p
                # nsurprising -= 1
            n += 1
        else:
            if g and nsurprising > 0 and v_ceil + 1 >= p:
                nsurprising -= 1
                n += 1
        # print 'G: ', g, ' i_triplet: ', m_triplet
    return 'Case #%d: %d' % (cas, n)
    
if __name__ == '__main__':
    import sys
    f = sys.stdin
    T = int(f.readline())
    for tc in range(1, T + 1):
        l = f.readline().strip('\n').split(' ')
        ngooglers = int(l[0])
        nsurprising = int(l[1])
        p = int(l[2])
        scores = [int(x) for x in l[3:]]
        print count_dancers_at(tc, ngooglers, nsurprising, p, scores)
    #import doctest
    #doctest.testmod()