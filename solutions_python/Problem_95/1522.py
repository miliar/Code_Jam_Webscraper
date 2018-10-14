rese=['ejp mysljylc kd kxveddknmc re jsicpdrysi',
      'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
      'de kr kd eoya kw aej tysr re ujdr lkgc jv']
eng=['our language is impossible to understand',
     'there are twenty six factorial possibilities',
     'so it is okay if you want to just give up']
d = {}
for i,reseline in enumerate(rese):
    engline = eng[i]
    for j,rc in enumerate(reseline):
        ec = engline[j]
        d[rc] = ec
# Add the hardcoded.
d['y'] = 'a'
d['e'] = 'o'
d['q'] = 'z'
# From inference.
d['z'] = 'q'

f = open('tongues.test','r')
cases = int(f.readline())
for case in range(cases):
    line = f.readline()
    trans = ''.join([d[ch] for ch in line.strip()])
    print 'Case #%s: %s' % (case+1, trans)
