l = [['ejp mysljylc kd kxveddknmc re jsicpdrysi',
    'our language is impossible to understand'],
    ['rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
        'there are twenty six factorial possibilities'],
    ['de kr kd eoya kw aej tysr re ujdr lkgc jv',
        'so it is okay if you want to just give up'],
    ]

s = [set(zip(a,b)) for [a,b] in l]
t = set()
for ss in s: 
    t = t | ss
mapa = dict(sorted(t))

def trad(frase):
    return ''.join([mapa[c] for c in frase])

def input(filename):
    with open(filename) as f:
        lines = f.read().split('\n')
        n = int(lines[0])
        return lines[1:n+1]

def process(lines):
    resp = [trad(l) for l in lines]
    resp = zip(xrange(1,len(resp)+1), resp)
    return ['Case #%s: %s\n' % (i,r) for (i,r) in resp]

def output(lines, filename):
    with open(filename, 'w') as f:
        f.writelines(lines)
