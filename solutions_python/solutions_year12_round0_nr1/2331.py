f = open("tongues.in", "r")

T = int(f.readline())

words_in = []
words_out = []

for i in range(0, T):
    words_in.append(f.readline())

f.close()



d = {}

d[' '] = ' '
d['\n'] = ''
d['a'] = 'y'
d['b'] = 'h'
d['c'] = 'e'
d['d'] = 's'
d['e'] = 'o'
d['f'] = 'c'
d['g'] = 'v'
d['h'] = 'x'
d['i'] = 'd'
d['j'] = 'u'
d['k'] = 'i'
d['l'] = 'g'
d['m'] = 'l'
d['n'] = 'b'
d['o'] = 'k'
d['p'] = 'r'
d['q'] = 'z'
d['r'] = 't'
d['s'] = 'n'
d['t'] = 'w'
d['u'] = 'j'
d['v'] = 'p'
d['w'] = 'f'
d['x'] = 'm'
d['y'] = 'a'
d['z'] = 'q'


def translate(word):
    out_word = ""
    for ltr in word:
        out_word += d[ltr]

    return out_word


for i in range(0, T):
    words_out.append(translate(words_in[i]))




f = open("tongues.out", "w")

for i in range(0, T):
    f.write("Case #" + str(i+1) + ": " + str(words_out[i]) + "\n")

f.close()

print "done"
