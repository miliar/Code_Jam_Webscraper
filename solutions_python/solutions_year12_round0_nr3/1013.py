def recycled(a,b):
    for n in xrange(a,b+1):
        _n = str(n)
        for i in xrange(1,len(_n)):
            _m = _n[i:] + _n[0:i]
            if _m[0] == '0':
                continue
            else:
                result = [int(_n),int(_m)]
                result.sort()
                yield result

if __name__ == '__main__':
    inp = file('C-small-attempt2.in', 'r')
    out = file('C-small-attempt2.out','w')
    i = 1
    n = inp.readline()

    for line in inp:
        seen = {}
        a,b = map(int,line.split())
        no = 0
        gen = recycled(a,b)
        for n,m in gen:
            if n >= a and m > n and m <= b:
                key = '%d,%d' % (n,m)

                try:
                    seen[key]
                except KeyError:
                    no += 1
                    seen[key] = True

        out.write('Case #%d: %d\n' % (i,no))
        i += 1

