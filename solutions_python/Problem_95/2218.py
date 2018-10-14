import sys

f = """ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv"""


t = """our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up"""

trans = dict((k,v) for k,v in zip(f,t))
trans['z'] = 'q'
trans['q'] = 'z'

with open(sys.argv[1], 'r') as fp:
    data = fp.read()
    lines = data.splitlines()[1:]
    for line_number, line in enumerate(lines):
        print("Case #%s: %s" % (line_number+1, ''.join(trans[c] for c in line)))
