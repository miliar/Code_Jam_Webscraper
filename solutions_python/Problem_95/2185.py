lol = { 'a':'y',
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
        ' ':' '
        }

def main(message):
    return "".join([lol[c] for c in message])


if __name__ == "__main__":
    for i in range(int(raw_input())):
        print("Case #{0}: {1}".format(i+1, main(raw_input())))
