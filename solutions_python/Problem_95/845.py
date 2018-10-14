f = open('data.txt', 'r')
g = open('data1.txt', 'w')

mapping = dict()
mapping['y'] = 'a'
mapping['n'] = 'b'
mapping['f'] = 'c'
mapping['i'] = 'd'
mapping['c'] = 'e'
mapping['w'] = 'f'
mapping['l'] = 'g'
mapping['b'] = 'h'
mapping['k'] = 'i'
mapping['u'] = 'j'
mapping['o'] = 'k'
mapping['m'] = 'l'
mapping['x'] = 'm'
mapping['s'] = 'n'
mapping['e'] = 'o'
mapping['v'] = 'p'
mapping['z'] = 'q'
mapping['p'] = 'r'
mapping['d'] = 's'
mapping['r'] = 't'
mapping['j'] = 'u'
mapping['g'] = 'v'
mapping['t'] = 'w'
mapping['h'] = 'x'
mapping['a'] = 'y'
mapping['q'] = 'z'
mapping[' '] = ' '

line = f.readline()
n = int(line)
for i in range(1, n+1):
    line = f.readline()
    string = ''
    for x in line:
        if x != '\n':
            string = string + mapping[x]
    result = "Case #" + str(i) + ": " + string + '\n'
    g.write(result)

f.close()
g.close()
