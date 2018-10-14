import sys, string
i = sys.stdin.readlines()
t, inputs = int(i[0]), [line.strip() for line in i[1:] if line.strip()]

samples = """
Case #1: our language is impossible to understand
Case #2: there are twenty six factorial possibilities
Case #3: so it is okay if you want to just give up

"""

outputs = [line.strip().split(': ')[1] for line in samples.splitlines() if line.strip()]

d = {'a':'y', 'o': 'e', 'z': 'q', 'q': 'z'}

for gog, eng in zip(inputs,outputs):
    for k, v in zip(gog, eng):
        d[k] = v
        
#for c in string.ascii_lowercase:
#    print c, d.get(c, 'MISSING')

for n, i in enumerate(inputs):
    print 'Case #%s: %s' % (n+1, ''.join([d.get(c, c) for c in i]))


