n = int(raw_input())

c = {' ': ' ',
 'a': 'y',
 'b': 'h',
 'c': 'e',
 'd': 's',
 'e': 'o',
 'f': 'c',
 'g': 'v',
 'h': 'x',
 'i': 'd',
 'j': 'u',
 'k': 'i',
 'l': 'g',
 'm': 'l',
 'n': 'b',
 'o': 'k',
 'p': 'r','q' : 'z',
 'r': 't',
 's': 'n',
 't': 'w',
 'u': 'j',
 'v': 'p',
 'w': 'f',
 'x': 'm',
 'y': 'a',
 'z': 'q'}


for i in xrange(0,n):
    p = raw_input()
    q = ['$'] * len(p)
    for j in xrange(0,len(p)):
        q[j] = c[p[j]]
    print "Case #%d: %s" % (i+1, "".join(q))    

