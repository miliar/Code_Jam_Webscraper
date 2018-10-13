import re

L, D, N = map(int, raw_input().split(' '))

palavras = []

for i in range(D):
    palavras.append(raw_input().strip())

for i in range(N):
    resp = 0
    l = raw_input().strip()
    pt = map(lambda x: x.strip('()'), re.findall('[a-z]|\([a-z]*\)', l))
    for p in palavras:
        for l1, l2 in zip(p, pt):
            if not l1 in l2:
                break
        else:
            resp += 1
    print 'Case #%d: %d' % (i+1, resp)


