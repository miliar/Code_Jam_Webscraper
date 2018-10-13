def rplc(dic, string):
    final = ''
    for w in string:
        if w == ' ':
            final += w
        elif w == '\n':
            pass
        else:
            final += dic[w]

    return final

translate = {
             'a': 'y',
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
             'q': 'z',  #
             'r': 't',
             's': 'n',
             't': 'w',
             'u': 'j',
             'v': 'p',
             'w': 'f',
             'x': 'm',
             'y': 'a',
             'z': 'q'   #
            }


arqv = open('A-small-attempt0.in', 'r')
n = arqv.readline()
output = ''

for i in range(int(n)):
    output += "Case #" + str(i + 1) + ': ' + rplc(translate, arqv.readline()) + "\n"

arqv.close()

out = file('output.txt', 'w+')
out.write(output)
out.close()
