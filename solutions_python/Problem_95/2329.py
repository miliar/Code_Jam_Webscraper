from common import nt, ni, nl, line

keys = 'aoz' + 'ejp mysljylc kd kxveddknmc re jsicpdrysi' + 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd' + 'de kr kd eoya kw aej tysr re ujdr lkgc jv' + 'q'
values = 'yeq' + 'our language is impossible to understand' + 'there are twenty six factorial possibilities' + 'so it is okay if you want to just give up' + 'z'

# Generate mapping
mapping = {}
for i,k in enumerate(keys):
    mapping[k] = values[i]
   
n = ni(); nl()
for case in xrange(n):
    text = ' '.join(line())
    text = ''.join([mapping[c] for c in text])
    print "Case #%s:" % (case+1),
    print text
