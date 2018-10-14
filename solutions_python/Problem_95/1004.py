#!/usr/bin/env python


import argparse
import sys


dictionary = dict(zip(('ejp mysljylc kd kxveddknmc re jsicpdrysi '
                       'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd '
                       'de kr kd eoya kw aej tysr re ujdr lkgc jv'),
                       ('our language is impossible to understand '
                       'there are twenty six factorial possibilities '
                       'so it is okay if you want to just give up')))
dictionary['z'] = 'q'
dictionary['q'] = 'z'
dictionary.update(dict(map(str.upper, item) for item in dictionary.iteritems()))


def solve(line):
    return ''.join(dictionary[char] for char in line)


def main(args):
    test_cases = next(args.input).strip()
    for case_index, line in enumerate(args.input, 1):
        print("Case #{}: {}".format(case_index, solve(line.strip())))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('--dictionary', type=argparse.FileType('r'),
                        default=open('/usr/share/dict/words'))
    main(parser.parse_args())
