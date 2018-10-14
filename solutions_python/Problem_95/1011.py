#!/usr/bin/env python3

import sys

samples = {
    'ejp mysljylc kd kxveddknmc re jsicpdrysi':
        'our language is impossible to understand',

    'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd':
        'there are twenty six factorial possibilities',

    'de kr kd eoya kw aej tysr re ujdr lkgc jv':
        'so it is okay if you want to just give up',

    'y': 'a',
    'e': 'o',
    'q': 'z',
    'z': 'q',
}


def make_decoder(samples):
    decoder = {}
    for googlese, english in samples.items():
        for g, e in zip(googlese, english):
            decoder[g] = e
    return decoder


def main(_):
    next(sys.stdin)    # Ignore number of cases line
    d = make_decoder(samples)
    for i, line in enumerate(sys.stdin, 1):
        line = line.strip()
        print('Case #{}: {}'.format(i, ''.join(d[c] for c in line)))

if __name__ == '__main__':
    main(sys.argv[1:])
