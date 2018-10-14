import sys

mapping = {}
mapping[' '] = ' '
mapping['a'] = 'y'
mapping['b'] = 'h'
mapping['c'] = 'e'
mapping['d'] = 's'
mapping['e'] = 'o'
mapping['f'] = 'c'
mapping['g'] = 'v'
mapping['h'] = 'x'
mapping['i'] = 'd'
mapping['j'] = 'u'
mapping['k'] = 'i'
mapping['l'] = 'g'
mapping['m'] = 'l'
mapping['n'] = 'b'
mapping['o'] = 'k'
mapping['p'] = 'r'
mapping['q'] = 'z'
mapping['r'] = 't'
mapping['s'] = 'n'
mapping['t'] = 'w'
mapping['u'] = 'j'
mapping['v'] = 'p'
mapping['w'] = 'f'
mapping['x'] = 'm'
mapping['y'] = 'a'
mapping['z'] = 'q'

filename = sys.stdin

count = int (filename.readline())
output = ""

for i in range(count):
    line = filename.readline().rstrip()
    output = output + "Case #" + str(i + 1) + ": "
    for char in line:
        output = output + mapping[char]
    if(i != count - 1):
        output = output + "\n"

print output


