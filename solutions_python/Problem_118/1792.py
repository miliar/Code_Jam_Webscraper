import math

def is_palindrome(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and is_palindrome(s[-1][1:])

with open('C-small-attempt0.in') as f:
    cases = int(f.readline())
    l = []
    r = []
    for c in xrange(cases):
        e = f.readline().split()
        l.append(int(e[0]))
        r.append(int(e[1]))

fair_square = []
for i in xrange(int(math.sqrt(1000))):
    if not is_palindrome(str(i)):
        continue
    if is_palindrome(str(i*i)):
        fair_square.append(i*i)

print fair_square
for i in xrange(len(l)):
    print 'Case #%s: %s' % (i+1, sum([j in fair_square for j in xrange(l[i], r[i]+1)]))

