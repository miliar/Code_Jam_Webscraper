def translate(sentence):
    new_s = ""
    for i in range (0, len(sentence)):
        new_s = new_s + m[sentence[i]]
    return new_s

m = {}
m['a'] = 'y'
m['b'] = 'h'
m['c'] = 'e'
m['d'] = 's'
m['e'] = 'o'
m['f'] = 'c'
m['g'] = 'v'
m['h'] = 'x'
m['i'] = 'd'
m['j'] = 'u'
m['k'] = 'i'
m['l'] = 'g'
m['m'] = 'l'
m['n'] = 'b'
m['o'] = 'k'
m['p'] = 'r'
m['q'] = 'z'
m['r'] = 't'
m['s'] = 'n'
m['t'] = 'w'
m['u'] = 'j'
m['v'] = 'p'
m['w'] = 'f'
m['x'] = 'm'
m['y'] = 'a'
m['z'] = 'q'
m[' '] = ' '

f = open("A-small-attempt1.in", "r")
w = open("out.txt", "w")

i = f.readline()
i = int(i.rstrip())
s = {}
for a in range (0, i):
    s[a] = f.readline().rstrip()

for a in range (0, i):
    w.write("Case #" + str(a+1) + ": " + translate(s[a]) + "\n")

f.close()
w.close()
