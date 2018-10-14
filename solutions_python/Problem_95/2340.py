#from pprint import pprint

f = open('3.in', 'r')
o = open('3.out', 'w')

#total
T = int(f.readline().strip())

#HINT = ["our language is impossible to understand",
#       "there are twenty six factorial possibilities",
#       "so it is okay if you want to just give up"]
#
#def make_trans():
#
#    translation = {}
#    for t in xrange(T):
#        #(n, m, o) = map(int, f.readline().strip().split(' '))
#        l = f.readline().strip()
#        for i, c in enumerate(l):
#            char_to = HINT[t][i]
#            translation[c] = char_to
#            print c, char_to
#
#    #given
#    translation['a'] = 'y'
#    translation['o'] = 'e'
#    translation['z'] = 'q'
#
#    return translation
#
#
#translation = make_trans()
#pprint(translation)

translation = {' ': ' ',
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
 'p': 'r',
 'r': 't',
 's': 'n',
 't': 'w',
 'u': 'j',
 'v': 'p',
 'w': 'f',
 'x': 'm',
 'y': 'a',
 'z': 'q',
 'q': 'z'}

for t in xrange(T):
    #(n, m, o) = map(int, f.readline().strip().split(' '))
    l = f.readline().strip()

    #res = str(n) + str(m) + str(o) + l

    res = ""
    for c in l:
        res += translation[c]

    s = "Case #%d: %s\n" % (t+1, res)
    print s
    o.write(s)


