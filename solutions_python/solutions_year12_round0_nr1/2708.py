
cases = open('language.txt').readlines()[1:]


translation = dict(zip(*reversed(zip(*({
 'a': 'y',
 'b': 'n',
 'c': 'f',
 'd': 'i',
 'e': 'c',
 'f': 'w',
 'g': 'l',
 'h': 'b',
 'i': 'k',
 'j': 'u',
 'k': 'o',
 'l': 'm',
 'm': 'x',
 'n': 's',
 'o': 'e',
 'p': 'v',
 'q': 'z',
 'r': 'p',
 's': 'd',
 't': 'r',
 'u': 'j',
 'v': 'g',
 'w': 't',
 'x': 'h',
 'y': 'a',
 'z': 'q'}.items())))))

def translate(letter):
    return translation.get(letter, letter)

with open('language-out.txt', 'wb') as output:
    for i, case in enumerate(cases):
        msg = ''.join(map(translate, case))
        output.write("Case #{i}: ".format(i=i + 1) + msg)
        print msg,
