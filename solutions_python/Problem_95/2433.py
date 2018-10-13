import sys
import string

f = open(sys.argv[1], 'r')

# First line has the number of lines to translate, we don't care.
f.readline()

# Variables
i = 1
out = ''
mapping_e_to_g = {
    'a': 'y', 'b': 'n', 'c': 'f', 'd': 'i', 'e': 'c', 'f': 'w',
    'g': 'l', 'h': 'b', 'i': 'k', 'j': 'u', 'k': 'o', 'l': 'm',
    'm': 'x', 'n': 's', 'o': 'e', 'p': 'v', 'q': 'z', 'r': 'p',
    's': 'd', 't': 'r', 'u': 'j', 'v': 'g', 'w': 't', 'x': 'h',
    'y': 'a', 'z': 'q', ' ': ' '
}
mapping_g_to_e = dict([[v,k] for k,v in mapping_e_to_g.items()])

# Now loop through the rest of the lines.
while True:
    contents = f.readline()
    contents = str.strip(contents)
    if contents != '':
        words = ''.join(map(lambda x: mapping_g_to_e[x], contents))
        line = ''.join(('Case #', str(i), ': ', words, '\n'))
        out = ''.join((out, line))
        i = i + 1
    if contents == '':
        break

print out

