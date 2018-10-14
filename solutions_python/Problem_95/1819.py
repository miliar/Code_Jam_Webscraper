import sys

def main():
    d = {'y': 'a', 'e': 'o', 'q': 'z'}
    clear = ('our language is impossible to understand there are twenty six factorial'
             'possibilities so it is okay if you want to just give up')
    cypher = ('ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym'
              'veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv')
    for c, z in zip(clear, cypher):
        if z in d: assert d[z] == c
        else: d[z] = c
    alphabet = set('abcdefghijklmnopqrstuvwxyz ')
    cyphermiss = alphabet - set(d.keys())
    clearmiss = alphabet - set(d.values())
    assert len(clearmiss) < 2 and len(clearmiss) == len(cyphermiss)
    d[cyphermiss.pop()] = clearmiss.pop()

    
    fin = open(sys.argv[1])
    with open(sys.argv[2], 'wb') as fout:
        T = int(fin.readline())
        for t in range(T):
            cypher = fin.readline().strip()
            clear = ''.join(d[z] for z in cypher)
            print >>fout, 'Case #%d: %s' % (t+1, clear)


if __name__ == '__main__':
    main()
