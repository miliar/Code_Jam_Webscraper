def main():
    f = open('A-small-attempt0.in')
    cases = f.readline()
    cur = 1
    for line in f.readlines(): 
        print "Case #%d: %s" % (cur, untranslate(line))
        cur += 1
    f.close()
    return

tr ={   'a': 'y',
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
        'z': 'q',
        ' ': ' '}


def untranslate(gin):
    res = ""
    for c in gin:
        if c != '\n':
            res += tr[c]
    return res

if __name__ == "__main__":
    main()
