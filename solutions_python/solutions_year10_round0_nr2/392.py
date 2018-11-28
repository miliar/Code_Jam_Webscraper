def gcd_l(lst):
    """
    Return gcd of list of integers.
    """
    import fractions as fractions
    g = lst[0]
    for j in range(1, len(lst)):
        g = fractions.gcd(g, lst[j])
        if g == 1:
            break
    return g
        

if __name__ == '__main__':
    openfile = open('B.in', 'r')
    C = int(openfile.readline()[:-1])
    for X in range(C):
        Nt = openfile.readline()[:-1]
        t = Nt.split(' ')
        #print t
        N = int(t[0])
        t.remove(t[0])
        t = [long(s) for s in t]
        #print t
        mn = t[0]
        for j in range(N):
            if t[j] < mn:
                mn = t[j]
        #print t
        lst = [s - mn for s in t]
        T = gcd_l(lst)
        if (mn % T) == 0:
            y = 0
        else:
            y = T - (mn % T)
        print 'Case #%s: %s' %(X+1, y)

    openfile.close()
