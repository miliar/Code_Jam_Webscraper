from collections import defaultdict

def read(filename):
    f = open(filename)
    t = int(f.readline())

    for i in xrange(t):
        n, m = map(int, f.readline().split(' '))
        yield i, [f.readline().rstrip() for j in xrange(n)], [f.readline().rstrip() for line in xrange(m)]


# We use a recursive defaultdict for string parts.
d = lambda: defaultdict(d)

def count(k, v, context):
    total = int(not context.has_key(k))

    for subkey, subval in v.iteritems():
        total += count(subkey, subval, context[k])
        
    return total


def output(*data):
    i, nvals, mvals = data
    existdict = d()
    createdict = d()
    
    for lines, dst in ((nvals, existdict), (mvals, createdict)):
        for src in lines:
            context = dst
            for part in src[1:].split('/'):
                context = context[part]

    result = sum(count(k, v, existdict) for k, v in createdict.iteritems())

    return 'Case #%i: %i\n' % (i + 1, result)


cases = read('test.in')

fout = open('result.txt', 'w')

for data in read('A-large.in'):
    fout.write(output(*data))
