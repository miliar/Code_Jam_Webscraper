#!/usr/bin/env python
import sys

cipher = 'ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv'
decoded = 'ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup'
assert len(cipher) == len(decoded)

def main(source):
    translation = {'q': 'z', 'y': 'a', 'e': 'o'}
    for (c, d) in zip(cipher, decoded):
        if c in translation:
            assert (d == translation[c])
        else:
            translation[c] = d
    az = set([chr(c) for c in range(ord('a'), ord('z')+1)])
    c, = (az - set(translation.keys()))
    d, = (az - set(translation.values()))
    translation[c] = d
    assert len(translation) == 26
    translation[' '] = ' '
    next(sys.stdin)
    for i, l in enumerate(sys.stdin):
        print('Case #%d: %s' % (i+1, ''.join(translation[c] for c in l.strip())))

if __name__ == '__main__':
    main(sys.stdin)
