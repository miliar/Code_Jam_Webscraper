def count_recycled(A,B):
    pairs = set()

    for v in xrange(A, B+1):
        s = str(v)

        for i in xrange(1,len(s)):
            (a,b) = sorted((v,int(s[i:] + s[:i])))

            if a >= A and a <= B and b >= A and b <= B and a != b:
                pairs.add((a,b))

    return len(pairs)

base = 'C-large'
with open(base + '.in','rb') as f:
    with open(base + '.out','wb') as fout:
        count = int(next(f))

        for (idx, l) in enumerate(f):
            (a,b) = map(int, l.split(' '))

            fout.write('Case #%d: %d\n' % (idx+1, count_recycled(a,b)))

            fout.flush()
