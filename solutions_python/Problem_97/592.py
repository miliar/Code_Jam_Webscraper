rf = open('C-large.in')

for i,line in enumerate(rf):
    if i==0: continue
    a,b = [int(x) for x in line.split(" ")]
    allpairs = set()
    for n in range(a,b+1):
        rot_n = str(n)
        def rotate(rot_n):
            return rot_n[-1]+rot_n[:-1]
        rot_n = rotate(rot_n)
        while int(rot_n) != n:
            m = int(rot_n)
            if m<=b and m>n and str(m) == rot_n: allpairs.add((n,m))
            rot_n = rotate(rot_n)
    print "Case #%s: %s" % (i,len(allpairs))


