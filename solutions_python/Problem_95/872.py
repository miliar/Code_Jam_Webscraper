#!/usr/bin/env python

def read_int():
    return int(raw_input())


tr = dict(y='a', e='o', q='z', z='q')

def learn(cipher, plain):
    for c, p in zip(cipher, plain):
        assert c not in tr or tr[c] == p
        tr[c] = p

learn('ejp mysljylc kd kxveddknmc re jsicpdrysi',
      'our language is impossible to understand')
learn('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
      'there are twenty six factorial possibilities')
learn('de kr kd eoya kw aej tysr re ujdr lkgc jv',
      'so it is okay if you want to just give up')


def do_case():
    return ''.join(tr[c] for c in raw_input())

def main():
    for case in xrange(read_int()):
        print 'Case #%d: %s' % (case + 1, do_case())


if __name__ == '__main__':
    main()
