#!/usr/bin/python
import sys

ENGLISH = ['o', 'u', 'r', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e', 'i', 's', 'i',
           'm', 'p', 'o', 's', 's', 'i', 'b', 'l', 'e', 't', 'o', 'u', 'n', 'd',
           'e', 'r', 's', 't', 'a', 'n', 'd', 't', 'h', 'e', 'r', 'e', 'a', 'r',
           'e', 't', 'w', 'e', 'n', 't', 'y', 's', 'i', 'x', 'f', 'a', 'c', 't', 
           'o', 'r', 'i', 'a', 'l', 'p', 'o', 's', 's', 'i', 'b', 'i', 'l', 'i',
           't', 'i', 'e', 's', 's', 'o', 'i', 't', 'i', 's', 'o', 'k', 'a', 'y', 
           'i', 'f', 'y', 'o', 'u', 'w', 'a', 'n', 't', 't', 'o', 'j', 'u', 's', 
           't', 'g', 'i', 'v', 'e', 'u', 'p']

GOOGLERESE = ['e', 'j', 'p', 'm', 'y', 's', 'l', 'j', 'y', 'l', 'c', 'k', 'd', 'k',
              'x', 'v', 'e', 'd', 'd', 'k', 'n', 'm', 'c', 'r', 'e', 'j', 's', 'i', 
              'c', 'p', 'd', 'r', 'y', 's', 'i', 'r', 'b', 'c', 'p', 'c', 'y', 'p', 
              'c', 'r', 't', 'c', 's', 'r', 'a', 'd', 'k', 'h', 'w', 'y', 'f', 'r', 
              'e', 'p', 'k', 'y', 'm', 'v', 'e', 'd', 'd', 'k', 'n', 'k', 'm', 'k', 
              'r', 'k', 'c', 'd', 'd', 'e', 'k', 'r', 'k', 'd', 'e', 'o', 'y', 'a', 
              'k', 'w', 'a', 'e', 'j', 't', 'y', 's', 'r', 'r', 'e', 'u', 'j', 'd', 
              'r', 'l', 'k', 'g', 'c', 'j', 'v']

MAP = dict(zip(GOOGLERESE, ENGLISH))
MAP['q'] = 'z'
MAP['z'] = 'q'


N = int(sys.stdin.readline())
for i in xrange(N):
    words = sys.stdin.readline().split()
    ewords = []
    for word in words:
        ewords.append(''.join(([MAP[c] for c in word])))

    sys.stdout.write('Case #{0}: {1}\n'.format(i+1, ' '.join(ewords)))


