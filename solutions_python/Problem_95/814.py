asd = {}

asd['a'] = 'y'
asd['b'] = 'h'
asd['c'] = 'e'
asd['d'] = 's'
asd['e'] = 'o'
asd['f'] = 'c'
asd['g'] = 'v'
asd['h'] = 'x'
asd['i'] = 'd'
asd['j'] = 'u'
asd['k'] = 'i'
asd['l'] = 'g'
asd['m'] = 'l'
asd['n'] = 'b'
asd['o'] = 'k'
asd['p'] = 'r'
asd['q'] = 'z'
asd['r'] = 't'
asd['s'] = 'n'
asd['t'] = 'w'
asd['u'] = 'j'
asd['v'] = 'p'
asd['w'] = 'f'
asd['x'] = 'm'
asd['y'] = 'a'
asd['z'] = 'q'

case = 0
cases = -1
for line in open('../data/problema.in'):
    if cases == -1:
        cases = int(line)
        continue
    newline = []
    for letter in line:
        if letter != ' ' and letter != '\n':
            newline.append(asd[letter])
        if letter == ' ':
            newline.append(' ')
    case += 1
    print 'Case #' + str(case) + ': ' + ''.join(newline)
   
