m = {' ': ' ', 'a': 'y', 'c': 'f', 'b': 'n', 'e': 'c', 'd': 'i', 'g': 'l', 'f':
        'w', 'i': 'k', 'h': 'b', 'k': 'o', 'j': 'u', 'm': 'x', 'l': 'm', 'o':
        'e', 'n': 's', 'q': 'z', 'p': 'v', 's': 'd', 'r': 'p', 'u': 'j', 't':
        'r', 'w': 't', 'v': 'g', 'y': 'a', 'x': 'h', 'z': 'q'}

newm = {}
for x, y in m.items():
    newm[y] = x

T = input()
n = 1
for t in xrange(T):
    i = raw_input()
    o = []
    for c in i:
        o.append(newm[c])
    print "Case #%d: %s" % (n, "".join(o))
    n += 1

