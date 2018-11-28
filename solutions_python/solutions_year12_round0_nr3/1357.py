import sys

def give_recyclers(x):
    l = len(x)
    generated_rs = []
    for i in xrange(l-1, -1, -1):
        if i > 0:
            r = x[-i:] + x[:l-i]
            if r != x and r not in generated_rs:
                generated_rs.append(r)
                yield r

def recycles_count_on_vector(n,m):
    recycles = []
    for x in xrange(n, m+1):
        for r in give_recyclers(str(x)):
            r = int(r)
            if r >= n and r <= m:
                recycles.append(r)
    return len(recycles) / 2

def run(f):
    testcases = f.next()
    for i, line in enumerate(f):
        print 'Case #%s:' % (i + 1), recycles_count_on_vector(*map(int, line.split(' ')))

if __name__ == "__main__":
    assert set(give_recyclers('23')) == set(['32'])
    assert set(give_recyclers('32')) == set(['23'])
    assert set(give_recyclers('321')) == set(['132', '213'])
    assert recycles_count_on_vector(10, 40) == 3
    f = open(sys.argv[1])
    run(f)
    f.close()
