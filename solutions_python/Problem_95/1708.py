import string

ciphers = ['y qee',
    'ejp mysljylc kd kxveddknmc re jsicpdrysi',
    'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
    'de kr kd eoya kw aej tysr re ujdr lkgc jv']
plains = ['a zoo',
    'our language is impossible to understand',
    'there are twenty six factorial possibilities',
    'so it is okay if you want to just give up']

enc = {}
dec = {}

for cipher, plain in zip(ciphers, plains):
    assert len(cipher) == len(plain)
    for c, p in zip(cipher, plain):
        if dec.get(c, p) != p:
            print '%s already decodes as %s (as well as %s)' % (c, dec[c], p)
        if enc.get(p, c) != c:
            print '%s already encodes as %s (as well as %s)' % (p, enc[p], c)
        enc[p] = c
        dec[c] = p

letters = set(string.lowercase + ' ')
missing_cipher = letters - set(dec.keys())
missing_plain = letters - set(enc.keys())
assert len(missing_cipher) == len(missing_plain) == 1

for c, p in zip(missing_cipher, missing_plain):
    enc[p] = c
    dec[c] = p

T = int(raw_input())
for cas in xrange(1, T+1):
    cipher = raw_input()
    print 'Case #%i:' % cas, ''.join(map(dec.get, cipher))
