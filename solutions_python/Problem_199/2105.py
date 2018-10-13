#!/usr/bin/env python

def invert(faces, x, y):
    for idx in xrange(x, y):
        faces[idx] = '+' if faces[idx] == '-' else '-'

for t in xrange(1, input()+1):
    faces, K = raw_input().strip().split()
    faces, K, L = list(faces), int(K), len(faces)

    count = 0
    for idx in xrange(L - K + 1):
        if faces[idx] == '-':
            invert(faces, idx, idx + K)
            count += 1

    print 'Case #{}: {}'.format(t, 'IMPOSSIBLE' if '-' in faces else count)
