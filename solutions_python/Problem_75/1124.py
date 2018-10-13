def magicka(C,D,N,combs,opp,xs):
    it = iter(xs)
    a=it.next()
    ans=[a]
    setans=set(ans)
    while True:
        try: b = it.next()
        except StopIteration: break
        if a+b in combs or b+a in combs:
            ans[-1]=a=combs[a+b]
            setans = set(ans)
        elif opp.get(b, 0) in setans:
            try:
                a = it.next()
                ans=[a]
                setans=set(ans) 
            except StopIteration:
                ans = []
                break
        else:
            ans.append(b)
            a=b
            setans.add(b)
    return repr(ans).replace("'","")

if __name__ == '__main__':
    bases=set(['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F'])
    fi = open('inputB.txt', 'r')
    fo = open('outputB.txt', 'w')
    T = int(fi.readline().strip('\n\r '))
    for ix in xrange(1,T+1):
        ls = fi.readline().strip('\n\r ').split(' ')
        C = int(ls[0])
        combs = {}
        for i in xrange(1,C+1):
            a,b,c=ls[i]
            combs[a+b]=c
            combs[b+a]=c
        D = int(ls[C+1])
        opp = {}
        for i in xrange(C+2, C+D+2):
            a,b=ls[i]
            opp[a]=b
            opp[b]=a
        N = int(ls[C+1+D+1])
        res = magicka(C,D,N,combs,opp,ls[1+C+1+D+1])
        #print res
        fo.write('Case #%d: %s\n' % (ix, res))
