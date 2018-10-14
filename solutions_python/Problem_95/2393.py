G = {' ': ' ', 'a': 'y', 'c': 'f', 'b': 'n', 'e': 'c', 'd': 'i', 'g': 'l', 'f': 'w', 'i': 'k', 'h': 'b', 'k': 'o', 'j': 'u', 'm': 'x', 'l': 'm', 'o': 'e', 'n': 's', 'q': 'z', 'p': 'v', 's': 'd', 'r': 'p', 'u': 'j', 't': 'r', 'w': 't', 'v': 'g', 'y': 'a', 'x': 'h', 'z': 'q'}
Gi = {}
for x in G:
    Gi[G[x]] = x


inp = open('c:/temp/A-small-attempt0.in')
out = open('c:/temp/A-small-attempt0.out', 'w')

n = int(inp.readline())
for i in xrange(1, n+1):
    gi = [Gi[x] for x in inp.readline().strip()]
    s = ''.join(gi)
    out.write('Case #%d: %s\n' % (i, s))

inp.close()
out.close()
    
