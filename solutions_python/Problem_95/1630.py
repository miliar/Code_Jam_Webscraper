
import sys

d = {'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}


T = int(sys.stdin.readline())
for t in xrange(T):
    print "Case #%d: %s" % (t+1, ' '.join(map(lambda word: ''.join([d[c] for c in word]), sys.stdin.readline().rstrip().split(' '))))


"""
d = {}

def process(b,a):
    w1 = a.split(' ') # human correct
    w2 = b.split(' ') # translated

    for i in range(len(w1)):
        for j in range(len(w1[i])):
            if w1[i][j] not in d:
                d[w1[i][j]] = w2[i][j]


d['z'] = 'q'
d['q'] = 'z'
process("our language is impossible to understand", "ejp mysljylc kd kxveddknmc re jsicpdrysi")
process("there are twenty six factorial possibilities", "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd")
process("so it is okay if you want to just give up", "de kr kd eoya kw aej tysr re ujdr lkgc jv")
print d
"""
