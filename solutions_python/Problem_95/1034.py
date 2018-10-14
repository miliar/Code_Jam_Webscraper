import sys

trans = {
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
        '\n':'\n'}

inp = sys.argv[1]
out = sys.argv[2]

with open(inp, 'r') as f:
    lines = f.readlines()
    n = int(lines[0][0])
    count = 1
    for ln in lines[1:]:
        with open(out, 'a') as output:
            output.write('Case #{0}: '.format(count))
            count += 1
            for i in ln:
                output.write(trans[i])

