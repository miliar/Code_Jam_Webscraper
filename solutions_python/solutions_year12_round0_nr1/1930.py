import sys

a = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv z q"
b = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up q z"

def solve(s):
    return "".join([b[a.find(c)] for c in s])

for i in xrange(int(raw_input())):
    s = sys.stdin.readline().strip()
    print 'Case #%d: %s' % (i+1, solve(s))
