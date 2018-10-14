import sys
in_file = sys.argv[1]
f = open(in_file, 'r')
input_array,output_array = [],[]
for line in f:
    input_array += [line.rstrip()]
input_array = input_array[1::]
def trans_letter(i):
    if i == ' ': return ' '
    elif i == 'a': return 'y'
    elif i == 'b': return 'h'
    elif i == 'c': return 'e'
    elif i == 'd': return 's'
    elif i == 'e': return 'o'
    elif i == 'f': return 'c'
    elif i == 'g': return 'v'
    elif i == 'h': return 'x'
    elif i == 'i': return 'd'
    elif i == 'j': return 'u'
    elif i == 'k': return 'i'
    elif i == 'l': return 'g'
    elif i == 'm': return 'l'
    elif i == 'n': return 'b'
    elif i == 'o': return 'k'
    elif i == 'p': return 'r'
    elif i == 'q': return 'z'
    elif i == 'r': return 't'
    elif i == 's': return 'n'
    elif i == 't': return 'w'
    elif i == 'u': return 'j'
    elif i == 'v': return 'p'
    elif i == 'w': return 'f'
    elif i == 'x': return 'm'
    elif i == 'y': return 'a'
    elif i == 'z': return 'q'
    else: return i
def translate(case):
    ret = ''
    for i in case:
        ret += '' + trans_letter(i)
    return ret
for case in input_array:
    output_array += ['Case #'+str(len(output_array)+1)+': '+translate(case)]
for line in output_array:
    print line
