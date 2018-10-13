import sys

inverse_key = {
    'a': 'y', 'b': 'n', 'c': 'f', 'd': 'i',
    'e': 'c', 'f': 'w', 'g': 'l', 'h': 'b',
    'i': 'k', 'j': 'u', 'k': 'o', 'l': 'm', 
    'm': 'x', 'n': 's', 'o': 'e', 'p': 'v', 
    'q': 'z', 'r': 'p', 's': 'd', 't': 'r', 
    'u': 'j', 'v': 'g', 'w': 't', 'x': 'h', 
    'y': 'a', 'z': 'q', ' ': ' '
}

key = { v:k for k,v in inverse_key.iteritems() }

result_tmpl = "Case #%d: %s"

f = sys.stdin
lines = int(f.readline())

for i in xrange(lines):
    s = ''.join([key[c] for c in f.readline().strip()])
    print result_tmpl % (i+1, s)