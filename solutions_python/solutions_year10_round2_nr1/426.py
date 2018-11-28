def gcjmain1():
    f = open('C:/456.in')
    fs = f.read().split('\n')
    out = file("sample.out", 'w')
    nc = int(fs[0])
    ln = 1
    md = 0
    tot = nc
    while nc > 0:
        n = int(fs[ln].split(' ')[0])
        m = int(fs[ln].split(' ')[1])

        have = fs[ln+1:ln+n+1]
        need = fs[ln+n+1:ln+n+m+1]
        nodes = []
        
        for p in need:
            while p not in have:
                have.append(p)
                md += 1
                p = '/'.join(p.split('/')[:-1])                        

        if '' in have:
            md -= 1

        #print "Case #%d: %d" % (tot - nc + 1, md)
        out.write("Case #%d: %d\n" % (tot - nc + 1, md))
        
        ln += (n + m + 1)
        nc -= 1
        md = 0
        
