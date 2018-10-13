#!/usr/bin/env python

def flip(faces, fr, to):
    for idx in xrange(fr, to):
        faces[idx] = '+' if faces[idx] == '-' else '-'

for t in xrange(1, input()+1):
    faces, K = raw_input().strip().split()
    faces, K, L = list(faces), int(K), len(faces)

    count = 0
    for idx in xrange(L - K + 1):
        if faces[idx] == '-':
            count += 1
            flip(faces, idx, idx + K)

    print 'Case #{}: {}'.format(t, 'IMPOSSIBLE' if '-' in faces else count)
