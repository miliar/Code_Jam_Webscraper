import sys, math, bisect

ispal = lambda i: str(i)[::-1] == str(i)

palsqs = []

i = 0
while i <= 2001002:
    if ispal(i) and ispal(i**2):
        palsqs.append(i)
        print >>sys.stderr,i
    i += 1
print >>sys.stderr,'ready'

def run_case():
    a,b = map(int,raw_input().split())
    art = int(math.ceil(a**0.5))
    brt = int(math.floor(b**0.5))
    print >>sys.stderr, bisect.bisect_left(palsqs,art), bisect.bisect_right(palsqs,brt)
    return bisect.bisect_right(palsqs,brt) - bisect.bisect_left(palsqs,art)

for i in xrange(int(raw_input())):
    print >>sys.stderr,(i+1)
    ans = run_case()
    print 'Case #%d:' % (i+1), ans
