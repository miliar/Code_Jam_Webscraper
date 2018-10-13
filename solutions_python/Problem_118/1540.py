table = {}

def palind(i):
    v = str(i)
    l = len(v)
    for j in xrange(l/2+1):
        if v[j] != v[l-j-1]:
            return False
    #print v
    return True

def build():
    global table
    upper = 10 ** 7
    table = dict([(i ** 2, True) for i in xrange(1, upper)
                  if palind(i ** 2) and palind(i)])

def solve(a, b):
    return len([x for x in table.iterkeys() if a <= x <= b])

build()
t = int(raw_input())
for i in xrange(t):
    a, b = map(int, raw_input().strip().split())
    print "Case #{0}: {1}".format(i + 1, solve(a, b))
