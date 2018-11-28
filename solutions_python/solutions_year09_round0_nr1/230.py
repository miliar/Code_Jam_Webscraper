import sys
import re

(L,D,N) = map(int,sys.stdin.readline().split(' '))

vocab = []
for d in range(D):
    vocab.append(sys.stdin.readline()[:L])

for n in range(N):
    pattern = re.sub('\(','[',sys.stdin.readline().strip())
    pattern = re.sub('\)',']',pattern)
    pattern = '^%s$' % pattern

    matches = 0
    for word in vocab:
        if re.match(pattern, word):
            matches += 1

    print "Case #%d: %d" % (n+1, matches)
