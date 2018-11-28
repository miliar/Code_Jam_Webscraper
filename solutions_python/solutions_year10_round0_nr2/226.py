import sys

def gcd(a, b):
    while 0 != a % b and 0 != b % a:
        if a > b:
            a = a % b
        else:
            b = b % a
    if a > b: return b
    else: return a

def run(events):
    events = [x for x in set(events)]
    diffs = [abs(x - y) for x, y in zip(events[:-1], events[1:])]
    curr = diffs[0]
    for next in diffs[1:]:
        curr = gcd(curr, next)
    n = events[0]
    if n % curr == 0 : return 0
    else: return curr - n % curr 

f = open(sys.argv[1])
num_cases = int(f.next())
for i in xrange(1, num_cases + 1):
    x = [long(a) for a in f.next().split(' ')]
    print 'Case #%i: %i'%(i, run(x[1:]))
