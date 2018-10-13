import sys
mapping = {
       ' ':' ',
       'a':'y',
       'b':'h',
       'c':'e',
       'd':'s',
       'e':'o',
       'f':'c',
       'g':'v',
       'h':'x',
       'i':'d',
       'j':'u',
       'k':'i',
       'l':'g',
       'm':'l',
       'n':'b',
       'o':'k',
       'p':'r',
       'q':'z',
       'r':'t',
       's':'n',
       't':'w',
       'u':'j',
       'v':'p',
       'w':'f',
       'x':'m',
       'y':'a',
       'z':'q',
}

def translate(line):
    output = ''
    for letter in line:
       if letter != '\n':
           output += mapping[letter]
    return output

std_input = sys.stdin.readlines()
cases = int(std_input.pop(0))

for case in range(cases):
    line = std_input[case]
    print 'Case #%s: %s' % (case+1, translate(line),)
