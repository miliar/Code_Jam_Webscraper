def recycled(A, B):
    lst = []
    for n in xrange(A, B+1):
        s = str(n)
        for i in xrange(len(s)):
            m = int(s[i:] + s[:i])
            if len(s) != len(str(m)):
                continue
            if m == n:
                continue
            if m > B or m < A:
                continue
            if (m, n) in lst or (n, m) in lst:
                continue
            lst.append((n, m))
            #print '%s is a recycled pair of %s'%(m,n)
    #print lst
    return len(lst)

def run(inpath, outpath):
    fin = open(inpath, 'rU')
    fout = open(outpath, 'w')

    for i, line in enumerate(fin):
        if not i:
            continue
        A, B = [int(n) for n in line.strip().split(' ')]
        val = recycled(A, B)
        print 'Case #{0}: {1}'.format(i, val)
        fout.write('Case #{0}: {1}\n'.format(i, val))

    fin.close()
    fout.close()
