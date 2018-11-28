#!/usr/bin/env python

import sys
from pprint import pprint

sample = [('ejp mysljylc kd kxveddknmc re jsicpdrysi',
           'our language is impossible to understand'),
          ('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
           'there are twenty six factorial possibilities'),
          ('de kr kd eoya kw aej tysr re ujdr lkgc jv',
           'so it is okay if you want to just give up')]

def learn():
    db = {}

    for (a, b) in sample:
        for i in range(len(a)):
            db[a[i]] = b[i]

    db['z'] = 'q'
    db['q'] = 'z'
    return db

def tr(s, db):
    return ''.join([db[x] for x in s])

def tongue():
    db = learn()

    count = int(sys.stdin.readline())
    for i in range(count):
        enc = sys.stdin.readline().strip()
        dec = tr(enc, db)
        print('Case #%d: %s' % (i+1, dec))

    #pprint(db)
    #pprint(tr(sample[0][0], db))


if __name__ == '__main__':
    tongue()
