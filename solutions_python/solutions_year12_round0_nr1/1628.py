def read_ints():
    a = raw_input().split()
    return [int(x) for x in a]

def read_int():
    return read_ints()[0]


mapping = {}
translated = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
              'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
              'de kr kd eoya kw aej tysr re ujdr lkgc jvqz']
original = ['our language is impossible to understand',
            'there are twenty six factorial possibilities',
            'so it is okay if you want to just give upzq']
for i in range(len(translated)):
    target = translated[i]
    orig = original[i]
    for c in range(len(target)):
        if target[c] in mapping:
            if mapping[target[c]] != orig[c]:
                raise 'Oh I got the problem statement wrong'
        mapping[target[c]] = orig[c]
        mapping[target[c].upper()] = orig[c].upper()

def solve():
    line = raw_input().strip()
    out = ''.join(mapping[c] for c in line)
    return out

if __name__ == '__main__':
    T = read_int()
    for i in range(T):
        print 'Case #%d: %s' % (i+1, solve())
