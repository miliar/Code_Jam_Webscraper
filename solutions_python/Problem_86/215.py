_case = 0
def gout(s):
    global _case
    _case += 1
    print "Case #%d: %s" % (_case,s) 

def memoize(f):
    dict = {}
    def func(*n):
        if n in dict:
            return dict[n]
        else:
            dict[n] = f(*n)
            return dict[n]
    return func

@memoize
def gcd(a,b):
    if not b: return a
    return gcd(b,a%b)

@memoize
def lcm(a,b):
    return a*b/gcd(a,b)

for _ in xrange(int(raw_input())):
    _,l,h = (int(x) for x in raw_input().split())
    notes = set(range(l,h+1))
    for n in (int(x) for x in raw_input().split()):
        gone = set()
        for note in notes:
            if note%n and n%note:
                gone.add(note)
        notes -= gone
    if notes:
        gout(sorted(list(notes))[0])
    else:
        gout('NO')
