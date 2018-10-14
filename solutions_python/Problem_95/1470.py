#!/usr/bin/env python3

d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}
d['q'] = 'z'
d['z'] = 'q'


def translate(G):
    return ''.join(list(map(lambda c: d[c], G)))


def main():
    with open('A.in') as fin, open('A.out', 'w') as fout:
        T = int(next(fin))
        for i, line in enumerate(fin):
            print('Case #%d:' % (i + 1), translate(line[:-1]), file=fout)


if __name__ == "__main__":
    main()
