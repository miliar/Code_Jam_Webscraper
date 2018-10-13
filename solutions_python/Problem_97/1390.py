def rot(n,cache={}):
    if n in cache:
        return set(cache[n])
    s = str(n)
    r = (s[i:]+s[:i] for i in xrange(len(s)))
    r = [int(i) for i in r if len(str(int(i))) == len(i)]
    cache[n] = tuple(r)
    return set(r)

def solve(a, b):
    counted = set()
    total = 0
    for i in xrange(a, b+1):
        x = rot(i)
        counted.add(i)
        total += len([z for z in x if z not in counted and a <= z <= b])
    return total


tests = int(raw_input())

for i in xrange(tests):
    a, b = map(int, raw_input().split(' '))
    print 'Case #%s:' % (i+1), solve(a, b)
