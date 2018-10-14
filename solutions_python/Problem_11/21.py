import sys

it = (e.strip("\n") for e in sys.stdin)
def gen(n):
    d = 10
    while d < n:
        first = n/d
        for rest in gen(n%d):
           yield first + rest
           yield first - rest
        d = d*10
    yield n

def gen2(parts):
    for i in range(1, len(parts)):
        first = int(parts[:i])
        for rest in gen2(parts[i:]):
            yield first+rest
            yield first-rest
    else:
        yield int(parts)

def isUgly(n):
    return n%2==0 or n%3 == 0 or n%5==0 or n%7 ==0 

for i in range(int(it.next())):
    #n = int(it.next())
    total = sum(1 if isUgly(e) else 0 for e in gen2(it.next()))
    print "Case #%i: %i" % (i+1, total)