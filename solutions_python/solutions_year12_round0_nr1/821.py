'''
Created on Apr 13, 2012

@author: dan
'''
import sys

if __name__ == '__main__':
    chars = 'abcdefghijklmnopqrstuvwxyz'
    ge = ['ejp mysljylc kd kxveddknmc re jsicpdrysi',
    'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
    'de kr kd eoya kw aej tysr re ujdr lkgc jv']
    en = ['our language is impossible to understand',
        'there are twenty six factorial possibilities',
        'so it is okay if you want to just give up']
    e2g = {'a': 'y', 'o': 'e', 'z': 'q'}
    g2e = {v: k for k, v in e2g.items()}
    for i in range(3):
        g, e = ge[i], en[i]
        assert len(g) == len(e)
        for j in range(len(g)):
            gc, ec = g[j], e[j]
            if gc == ' ':
                assert ec == ' '
                continue
            if gc in g2e:
                assert g2e[gc] == ec
                assert e2g[ec] == gc
            else:
                g2e[gc] = ec
                e2g[ec] = gc
    assert len(g2e) == len(e2g) == 25
    chars = set(chars)
    gk = chars.difference(g2e.keys()).pop()
    ek = chars.difference(e2g.keys()).pop()
    g2e[gk] = ek
    e2g[ek] = gk
    g2e[' '] = ' '

    def g_to_e(gtext):
        return ''.join([g2e[c] for c in gtext])

    lines = sys.stdin.readlines()
    T = int(lines[0])
    n = 1
    for G in lines[1:]:
        G = G.strip()
        print('Case #%d: %s' % (n, g_to_e(G)))
        n += 1


