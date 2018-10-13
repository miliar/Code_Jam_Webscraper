a = '''
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
'''
b = '''
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
'''

m = {' ': ' '}

for c in range(0, 26):
    ch = chr(ord('a') + c)
    try:
        i = a.index(ch)
        m[a[i]] = b[i]
    except ValueError:
        pass

m['\n'] = ''
m['q'] = 'z'
m['z'] = 'q'

f = open('a.in')
n = int(f.readline())

from StringIO import StringIO

for testcase in range(1, n + 1):
    s = f.readline()
    t = StringIO()
    for c in s:
        t.write(m[c])
    print 'Case #%d: %s' % (testcase, t.getvalue())
