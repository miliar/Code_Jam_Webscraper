import sys

mapping = {
    'y':'a',
    'n':'b',
    'f':'c',
    'i':'d',
    'c':'e',
    'w':'f',
    'l':'g',
    'b':'h',
    'k':'i',
    'u':'j',
    'o':'k',
    'm':'l',
    'x':'m',
    's':'n',
    'e':'o',
    'v':'p',
    'z':'q',
    'p':'r',
    'd':'s',
    'r':'t',
    'j':'u',
    'g':'v',
    't':'w',
    'h':'x',
    'a':'y',
    'q':'z',
    ' ':' '
}

sys.stdin.readline()
i = 1
for line in sys.stdin:
    print("Case #" + str(i) + ": " + ''.join([mapping[c] for c in line.strip()]))
    i += 1
