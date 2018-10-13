import numpy as np

if __name__ == '__main__':

    sample_in = ('ejp mysljylc kd kxveddknmc re jsicpdrysi'
                 + 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
                 + 'de kr kd eoya kw aej tysr re ujdr lkgc jv')
    sample_out = ('our language is impossible to understand'
                  + 'there are twenty six factorial possibilities'
                  + 'so it is okay if you want to just give up')

    # Build dictionary.
    d = {}
    for a, b in zip(sample_in, sample_out):
        d[a] = b

    # Add given letters.
    d['y'] = 'a'
    d['e'] = 'o'
    d['q'] = 'z'

    # Find missing letter.
    all_letters = [chr(x) for x in range(ord('a'), ord('z')+1)]
    a = [x for x in all_letters if x not in d.keys()]
    b = [x for x in all_letters if x not in d.values()]
    d[a[0]] = b[0]

    # Add enter for simplicity.
    d['\n'] = '\n'

    # Apply dictionary to text.
    ## f = open('input1a.txt')
    f = open('A-small-attempt0.in')
    f2 = open('output1.txt', 'w')
    n = int(f.readline())
    for i, y in enumerate(f.readlines()):
        z = ''.join([d[x] for x in y])
        print 'Case #%d: %s' % (i+1, z)
        f2.write('Case #%d: %s' % (i+1, z))
    f.close()
    f2.close()
