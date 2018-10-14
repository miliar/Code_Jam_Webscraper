#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#
# author: Álvaro Lázaro

import string

def main():
    out = ""
    translation = [
            ('y', 'a'),
            ('n', 'b'),
            ('f', 'c'),
            ('i', 'd'),
            ('c', 'e'),
            ('w', 'f'),
            ('l', 'g'),
            ('b', 'h'),
            ('k', 'i'),
            ('u', 'j'),
            ('o', 'k'),
            ('m', 'l'),
            ('x', 'm'),
            ('s', 'n'),
            ('e', 'o'),
            ('v', 'p'),
            ('z', 'q'),
            ('p', 'r'),
            ('d', 's'),
            ('r', 't'),
            ('j', 'u'),
            ('g', 'v'),
            ('t', 'w'),
            ('h', 'x'),
            ('a', 'y'),
            ('q', 'z')]
    translation = zip(*translation)
    translation = string.maketrans("".join(translation[0]),
        "".join(translation[1]))

    with open('in.txt', 'r') as f:
        lines = f.readlines()
        n = int(lines[0])
        for i in xrange(1, n + 1):
            original = lines[i]
            out += "Case #%s: %s" % (i, original.translate(translation))

    with open('out.txt', 'w') as out_file:
        out_file.write(out)


if __name__ == '__main__':
    main()
