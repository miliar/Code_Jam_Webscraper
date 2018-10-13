number_of_cases = int(raw_input())

trans = {
    'y':'a', 'n':'b', 'f':'c', 'i':'d', 'c':'e', 'w':'f',
    'l':'g', 'b':'h', 'k':'i', 'u':'j', 'o':'k', 'm':'l',
    'x':'m', 's':'n', 'e':'o', 'v':'p', 'z':'q', 'p':'r',
    'd':'s', 'r':'t', 'j':'u', 'g':'v', 't':'w', 'h':'x',
    'a':'y', 'q':'z', ' ':' '
    }

for i in range(1, number_of_cases + 1):
    out = ""

    for c in raw_input():
        out = out + trans[c]

    print "Case #" + str(i) + ": " + out
