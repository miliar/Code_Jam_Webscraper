f = open('A-small-attempt0.in','r')
o = open('output.txt','w')
cases = f.readline()

# encoding dictionary
words = {}
words['a'] = 'y'
words['b'] = 'n'
words['c'] = 'f'
words['d'] = 'i'
words['e'] = 'c'
words['f'] = 'w'
words['g'] = 'l'
#h
words['h'] = 'b'
words['i'] = 'k'
words['j'] = 'u'
words['k'] = 'o'
words['l'] = 'm'
words['m'] = 'x'
words['n'] = 's'
words['o'] = 'e'
words['p'] = 'v'
#q  missing b, z
words['q'] = 'z'
words['r'] = 'p'
words['s'] = 'd'
words['t'] = 'r'
words['u'] = 'j'
words['v'] = 'g'
words['w'] = 't'
words['x'] = 'h'
words['y'] = 'a'
words['z'] = 'q'

decoder = dict((v,k) for k,v in words.items())

for case in xrange(0, int(cases)):
    encoded = f.readline().strip()
    message = ""
    for c in encoded:
        if c == " ":
            message += " "
        else:
            message += decoder[c]
    ans = "Case #%d: %s" % (case + 1, message)
    o.write(ans + '\n')