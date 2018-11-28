samples = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
           'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
           'de kr kd eoya kw aej tysr re ujdr lkgc jv']
results = ['our language is impossible to understand',
           'there are twenty six factorial possibilities',
           'so it is okay if you want to just give up']

d = {' ':' ', 'y':'a', 'e':'o', 'q':'z'}

for ss, rs in zip(samples, results):
    for s, r in zip(ss, rs):
        d[s] = r

##for c in 'abcdefghijklmnopqrstuvwxyz ':
##    if c not in d:
##        print 'key %s not in d'%c
##    if c not in d.values():
##        print 'value %s not in d'%c

# add leftover value
d['z'] = 'q'

        
def decode(s, d):
    r = ''
    for c in s:
        r += d[c]
    return r

def run(inpath, outpath):
    fin = open(inpath, 'rU')
    fout = open(outpath, 'w')

    for i, line in enumerate(fin):
        if not i:
            continue
        val = decode(line.strip(), d)
        print 'Case #{0}: {1}'.format(i, val)
        fout.write('Case #{0}: {1}\n'.format(i, val))

    fin.close()
    fout.close()
