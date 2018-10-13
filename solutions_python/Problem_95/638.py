import string

trans_map = {
    'y': 'a',
    'e': 'o',
    'q': 'z',
    ' ': ' '}

training = [
    ('ejp mysljylc kd kxveddknmc re jsicpdrysi', 'our language is impossible to understand'),
    ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'there are twenty six factorial possibilities'),
    ('de kr kd eoya kw aej tysr re ujdr lkgc jv', 'so it is okay if you want to just give up'),
    ]

c_letters_left = set(string.letters[26:26*2] + ' ')
p_letters_left = set(string.letters[26:26*2] + ' ')

for (c, p) in trans_map.iteritems():
    c_letters_left.remove(c)
    p_letters_left.remove(p)

for (c, p) in training:
    for (c0, p0) in zip(c,p):
        
        if c0 in trans_map:
            if trans_map[c0] != p0:
                raise RuntimeError('Assumption violation')
        else:
            trans_map[c0] = p0
            c_letters_left.remove(c0)
            p_letters_left.remove(p0)


if len(c_letters_left) > 1 or len(p_letters_left) > 1:
    raise RuntimeError('Ambigous mapping')

trans_map[list(c_letters_left)[0]] = list(p_letters_left)[0]

with open('A-small-attempt0.in','rb') as f:
    with open('A-small-attempt0.out','wb') as fout:
        first_line = True
        for (idx, l) in enumerate(f):
            if first_line:
                count = int(l)
                first_line = False
                continue

            fout.write('Case #%d: %s\n' % (idx, ''.join(map(trans_map.__getitem__, l.strip()))))
