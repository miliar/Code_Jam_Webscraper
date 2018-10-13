a_file = open('A-small-attempt4.in')
numcases = int(a_file.readline())

lettermap = {'a': 'y'}
lettermap['b'] = 'h'
lettermap['c'] = 'e'
lettermap['d'] = 's'
lettermap['e'] = 'o'
lettermap['f'] = 'c'
lettermap['g'] = 'v'
lettermap['h'] = 'x'
lettermap['i'] = 'd'
lettermap['j'] = 'u'
lettermap['k'] = 'i'
lettermap['l'] = 'g'
lettermap['m'] = 'l'
lettermap['n'] = 'b'
lettermap['o'] = 'k'
lettermap['p'] = 'r'
lettermap['q'] = 'z'
lettermap['r'] = 't'
lettermap['s'] = 'n'
lettermap['t'] = 'w'
lettermap['u'] = 'j'
lettermap['v'] = 'p'
lettermap['w'] = 'f'
lettermap['x'] = 'm'
lettermap['y'] = 'a'
lettermap['z'] = 'q'
lettermap[' '] = ' '
#qz
#
for i in range(numcases):
    param = a_file.readline()
    output = ""
    for letter in param:
        if letter != "\n":
            output += lettermap[letter]
    
    print("Case #" + str(i + 1) + ": " + output)
