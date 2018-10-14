import sys

gs = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
s = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
sub = {}
for i in range(0, len(gs)):
    sub[gs[i]] = s[i]

#for i in sorted(permutation):
#    print i, " -> ", permutation[i]

#print sorted(permutation.values())

def transform(string, sub):
    return "".join(map(lambda x: sub[x], string))

if(sys.argv[1] == '1'):
    sub['q'] = 'q'
    sub['z'] = 'z'
else:
    sub['q'] = 'z'
    sub['z'] = 'q'

with file(sys.argv[2], 'r') as f:
    lines = f.readlines()
    num = int(lines[0].rstrip())
    for i in xrange(1, num + 1):
        print "Case #%d: %s" % (i, transform(lines[i].rstrip(), sub))

