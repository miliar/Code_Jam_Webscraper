# Google Code Jam Problem A: Speaking in Tongues
# Solution by Michael Reinhard

def decodeChar(character):
    if character == 'a': return 'y'
    elif character == 'b': return 'h'
    elif character == 'c': return 'e'
    elif character == 'd': return 's'
    elif character == 'e': return 'o'
    elif character == 'f': return 'c'
    elif character == 'g': return 'v'
    elif character == 'h': return 'x'
    elif character == 'i': return 'd'
    elif character == 'j': return 'u'
    elif character == 'k': return 'i'
    elif character == 'l': return 'g'
    elif character == 'm': return 'l'
    elif character == 'n': return 'b'
    elif character == 'o': return 'k'
    elif character == 'p': return 'r'
    elif character == 'q': return 'z'
    elif character == 'r': return 't'
    elif character == 's': return 'n'
    elif character == 't': return 'w'
    elif character == 'u': return 'j'
    elif character == 'v': return 'p'
    elif character == 'w': return 'f'
    elif character == 'x': return 'm'
    elif character == 'y': return 'a'
    elif character == 'z': return 'q'
    elif character == ' ': return ' '
    else: return ''

def decodeString(string):
    return ''.join(map(decodeChar, string))

numOfLines = input()
for line in range(numOfLines):
    string = raw_input()
    print "Case #" + str(line + 1) + ": " + decodeString(string)
