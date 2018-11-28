import os
fp = open('A-small-attempt2.in','r')
content = fp.read()
fp.close()

mapping = {'a': 'y',
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
           'q': 'z',
           'r': 't',
           's': 'n',
           't': 'w',
           'u': 'j',
           'v': 'p',
           'w': 'f',
           'x': 'm',
           'y': 'a',
           'z': 'q'}

outputs = []
contents = content.split('\n')

for cont in contents:
    if contents[0] == cont:
        continue
    tmp = ''
    for letter in cont: 
        if letter.isalpha():
            tmp += mapping[letter]
        else:
            tmp += letter
    outputs.append(tmp)

fp = open('A-small-attempt0.out','w')
for output in outputs:
    if outputs.index(output) >= int(contents[0]):
        break
    tmp = "Case #" + str(outputs.index(output) + 1) + ': ' + output + "\n"
    fp.write(tmp)
fp.close()

